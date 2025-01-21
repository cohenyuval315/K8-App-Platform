"use client"

import { useState } from "react";

export interface Option {
  label: string;
  value: string | boolean;
  onChange: (newValue: boolean) => void;
}

interface CollapsibleOptionsProps {
  options: Option[];
  title?: string;
}

export default function CollapsibleOptions({ options, title }: CollapsibleOptionsProps) {
  const [isVisible, setIsVisible] = useState<boolean>(false);

  return (
    <div>
      <button
        type="button"
        onClick={() => setIsVisible(!isVisible)}
        className="w-full text-sm text-blue-500 hover:underline text-left"
      >
        {isVisible ? `Hide ${title || "Options"}` : `Show ${title || "Options"}`}
      </button>
      {isVisible && (
        <div className="space-y-2 mt-2">
          {options.map((option) => (
            <label key={option.label} className="block text-sm">
              <input
                type="checkbox"
                checked={!!option.value}
                onChange={(e) => option.onChange(e.target.checked)}
                className="mr-2"
              />
              {option.label}
            </label>
          ))}
        </div>
      )}
    </div>
  );
}
