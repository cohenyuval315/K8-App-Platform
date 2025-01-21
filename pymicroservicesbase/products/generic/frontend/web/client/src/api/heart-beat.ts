import { interval, Subject, Subscription } from 'rxjs';
import { tap, switchMap, takeUntil } from 'rxjs/operators';

class Heartbeat {
  private static instance: Heartbeat;
  private intervalTime: number;
  private stopSubject: Subject<void>;
  private pauseSubject: Subject<void>;
  private heartbeat$: any; // Observable
  private subscription: Subscription | null;
  private isPaused: boolean;
  private callback: Function | null;

  private constructor(config: { intervalTime: number, callback?: Function }) {
    this.intervalTime = config.intervalTime;
    this.stopSubject = new Subject();
    this.pauseSubject = new Subject();
    this.heartbeat$ = null;
    this.subscription = null;
    this.isPaused = false;
    this.callback = config.callback || null; // Set the callback function
  }

  // Singleton pattern
  public static getInstance(config: { intervalTime: number, callback?: Function } = { intervalTime: 5000 }): Heartbeat {
    if (!Heartbeat.instance) {
      Heartbeat.instance = new Heartbeat(config);
    }
    return Heartbeat.instance;
  }

  // Start the heartbeat
  public start() {
    if (this.subscription) {
      console.log("Heartbeat is already running.");
      return;
    }

    console.log("Starting heartbeat...");

    this.heartbeat$ = interval(this.intervalTime).pipe(
      switchMap(() => {
        // Each interval, we check if we are paused
        return this.pauseSubject.pipe(
          takeUntil(this.stopSubject),
          tap(() => {
            if (this.isPaused) {
              console.log("Heartbeat is paused.");
            } else {
              console.log("Sending heartbeat to server...");
              // If a callback is defined, invoke it
              if (this.callback) {
                this.callback();
              } else {
                console.log("Server is still online!");
              }
            }
          })
        );
      })
    );

    this.subscription = this.heartbeat$.subscribe();
  }

  // Pause the heartbeat
  public pause() {
    if (this.isPaused) {
      console.log("Heartbeat is already paused.");
      return;
    }
    console.log("Pausing heartbeat...");
    this.isPaused = true;
    this.pauseSubject.next();
  }

  // Resume the heartbeat
  public resume() {
    if (!this.isPaused) {
      console.log("Heartbeat is already running.");
      return;
    }
    console.log("Resuming heartbeat...");
    this.isPaused = false;
    this.pauseSubject.next();
  }

  // Stop the heartbeat
  public stop() {
    console.log("Stopping heartbeat...");
    this.stopSubject.next();
    this.subscription?.unsubscribe();
    this.subscription = null;
    this.isPaused = false;
  }

  // Set a new callback function for the heartbeat
  public setCallback(callback: Function) {
    this.callback = callback;
  }
}

export { Heartbeat };
