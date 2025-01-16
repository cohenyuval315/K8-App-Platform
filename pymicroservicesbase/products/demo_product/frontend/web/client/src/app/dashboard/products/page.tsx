// import Layout from "@/components/general/layout/Layout";
import Card from "@/components/general/ui/Card";
import Charts from "@/components/general/ui/Charts";
import { config } from "@/config";
import { redirect } from "next/navigation";

export default async function Page() {

  return (
      <>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <Card title="Total Revenue" value="$3,456" percentage="+4.5%" />
          <Card title="Total Profit" value="$45.2K" percentage="+2.3%" />
          <Card title="Total Products" value="2,450" percentage="+1.5%" />
          <Card title="Total Users" value="3,456" percentage="+0.6%" />
        </div>
        <div className="mt-6">
          <Charts />
        </div>
      </>

  );
}
