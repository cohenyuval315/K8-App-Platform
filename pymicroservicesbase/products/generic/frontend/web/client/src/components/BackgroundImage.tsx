"use client"

export default function BackgroundImage() { // TODO change to HERO
  return (
    <img
        src="assets/worldmap.gif"
        alt="Animated GIF"
        // className="w-full h-full object-cover"
        style={{
          userSelect:"none",
          pointerEvents:"none"
        }}
    />
  );
}
