"use client"

interface DropdownSelectProps {
    options: string[];
    selected: string;
    onChange: (value: string) => void;
    label?: string;
  }

  export default function DropdownSelect({
    options,
    selected,
    onChange,
    label,
  }: DropdownSelectProps) {
    return (
      <div>
        {label && (
          <label
            htmlFor="dropdown-select"
            className="block text-sm font-medium text-gray-700"
          >
            {label}
          </label>
        )}
        <select
          id="dropdown-select"
          value={selected}
          onChange={(e) => onChange(e.target.value)}
          className="mt-1 w-full p-2 border border-gray-300 rounded-md"
        >
          {options.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </div>
    );
  }
