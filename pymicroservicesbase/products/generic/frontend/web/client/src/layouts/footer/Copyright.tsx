interface CopyrightProps {
    text: string;
  }

  const Copyright: React.FC<CopyrightProps> = ({ text }) => {
    return <p className="text-gray-400 text-center">{text}</p>;
  };

  export default Copyright;
