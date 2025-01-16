import { cache } from 'react'
import 'server-only'

export const preload = (id: string) => {
  void getItem(id)
}

export const getItem = cache(async (id: string) => {
  // ...
})


/**
 * Enhances a server-side async function with optional caching, preloading, and server-only enforcement.
 * @param asyncFn - The async function to enhance.
 * @param options - Configuration options to control caching, preloading, and other behaviors.
 * @returns An enhanced function with optional caching, preloading, and server-only enforcement.
 */
export function withServer<TArgs extends any[], TResult>(
  asyncFn: (...args: TArgs) => Promise<TResult>,
  options?: {
    /**
     * Enable caching for the function. Default: true.
     */
    cache?: boolean;
    /**
     * Enable preloading for the function. Default: true.
     */
    preload?: boolean;
    /**
     * Enable logging for debugging. Default: false.
     */
    enableLogging?: boolean;
    /**
     * Custom key transformer for caching (e.g., stringifying arguments). Default: JSON stringified arguments.
     */
    keyTransformer?: (...args: TArgs) => string;
  }
) {
  const {
    cache: useCache = true,
    preload: enablePreload = true,
    enableLogging = false,
    keyTransformer = JSON.stringify,
  } = options || {};

  // Create the base function (with or without caching)
  const baseFn = useCache ? cache(asyncFn) : asyncFn;

  // Optional preload wrapper
  const preload = enablePreload
    ? (...args: TArgs) => {
        if (enableLogging) {
          console.log(`Preloading data with args: ${keyTransformer(...args)}`);
        }
        void baseFn(...args);
      }
    : undefined;

  // Logging wrapper for the main function
  const wrappedFn = (...args: TArgs) => {
    if (enableLogging) {
      console.log(`Fetching data with args: ${keyTransformer(...args)}`);
    }
    return baseFn(...args);
  };

  // Attach preload if enabled
  return Object.assign(wrappedFn, { preload });
}
