import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Plus } from "lucide-react";

const FlowsPage = () => {
  const sampleFlows = [
    {
      id: 1,
      name: "Data Extraction Pipeline",
      description: "Data extraction from various sources",
      status: "active",
      lastModified: "2024-03-15",
    },
    {
      id: 2,
      name: "Image Recognition Workflow",
      description: "Image recognition using AI",
      status: "inactive",
      lastModified: "2024-02-10",
    },
    {
      id: 3,
      name: "Customer Support Automation",
      description: "Customer suppport automation using chatbots",
      status: "active",
      lastModified: "2024-04-01",
    },
    {
      id: 4,
      name: "Sales Forecast Model",
      description: "Sales forecast model based on data analisys",
      status: "active",
      lastModified: "2024-03-28",
    },
  ];

  return (
    <div className="flex flex-col items-center min-h-screen p-4">
      <div className="w-full max-w-6xl">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {sampleFlows.map((flow) => (
            <Card key={flow.id} className="h-full flex flex-col">
              <CardHeader>
                <CardTitle className="text-lg font-semibold">
                  {flow.name}
                </CardTitle>
                <CardDescription className="text-sm text-muted-foreground">
                  {flow.description}
                </CardDescription>
              </CardHeader>
              <div className="flex items-center justify-between p-4">
                <span
                  className={`text-sm font-medium ${
                    flow.status === "active"
                      ? "text-green-600"
                      : "text-gray-500"
                  }`}
                >
                  Status: {flow.status}
                </span>
                <span className="text-xs text-muted-foreground">
                  Last update: {flow.lastModified}
                </span>
              </div>
            </Card>
          ))}
        </div>
      </div>

      <div className="fixed bottom-10 right-10">
        <Button
          variant="default"
          size="lg"
          className="flex items-center justify-center gap-2"
          aria-label="Add new Flow"
        >
          <Plus className="h-5 w-5" />
          <span>Add Flow</span>
        </Button>
      </div>
    </div>
  );
};

export default FlowsPage;
