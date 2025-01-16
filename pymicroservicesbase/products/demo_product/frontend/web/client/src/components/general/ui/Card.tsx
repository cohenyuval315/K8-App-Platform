interface CardProps {
    title: string;
    value: string;
    percentage: string;
  }

  export default function Card({ title, value, percentage }: CardProps) {
    return (
      <div className="p-4 bg-white shadow rounded">
        <h3 className="text-sm font-medium text-gray-500">{title}</h3>
        <p className="mt-2 text-xl font-bold">{value}</p>
        <p className={`text-sm ${percentage.startsWith("+") ? "text-green-500" : "text-red-500"}`}>
          {percentage}
        </p>
      </div>
    );
  }
