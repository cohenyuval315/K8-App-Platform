import Link from "next/link";

export const description =
  "We are a forward-thinking company dedicated to delivering innovative solutions and unparalleled customer experiences. Our passion drives us to push boundaries and achieve excellence.";
export const headers = {
  title: "About Us",
  subtitle: "Empowering Ideas, Building Futures",
  mission: "Our Mission",
  vision: "Our Vision",
  journey: "Our Journey",
};

export default async function Page(){
  return (
    <div className="container mx-auto px-6 py-12 text-gray-800">
    <header className="text-center mb-12">
        <h1 className="text-4xl font-bold text-gray-900 mb-4">{headers.title}</h1>
        <p className="text-lg text-gray-600">{headers.subtitle}</p>
    </header>

    <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-3">{headers.mission}</h2>
        <p className="text-gray-700 leading-relaxed">
        We aim to inspire positive change by delivering solutions that make a real difference. Every project we
        undertake is driven by a commitment to quality and innovation.
        </p>
    </section>

    <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-3">{headers.vision}</h2>
        <p className="text-gray-700 leading-relaxed">
        Our vision is to be a leader in creating sustainable solutions that benefit businesses and communities
        alike. We are shaping a better tomorrow through collaboration and expertise.
        </p>
    </section>

    <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-3">{headers.journey}</h2>
        <p className="text-gray-700 leading-relaxed">{description}</p>
    </section>

    <div className="text-center mt-10">
        <Link href="/" className="inline-block bg-blue-600 text-white py-3 px-6 rounded-lg shadow hover:bg-blue-700">
        Back to Home
        </Link>
    </div>
    </div>
  );
};
