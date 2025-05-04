import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";

const FlowPage = () => {
  // Struktura danych zgodna z koncepcją Flows (specjalnych bloków akcji)

  const sampleFlows = [
    {
      id: 1,
      name: "Data Extraction Pipeline",
      description: "Automatyczne wyodrębnianie danych z różnych źródeł",
      status: "active",
      lastModified: "2024-03-15",
    },
    {
      id: 2,
      name: "Image Recognition Workflow",
      description: "System rozpoznawania obrazów z wykorzystaniem AI",
      status: "inactive",
      lastModified: "2024-02-10",
    },
    {
      id: 3,
      name: "Customer Support Automation",
      description: "Automatyzacja obsługi klienta z użyciem chatbotów",
      status: "active",
      lastModified: "2024-04-01",
    },
    {
      id: 4,
      name: "Sales Forecast Model",
      description: "Model prognozowania sprzedaży oparty na analizie danych",
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
                  Ostatnia aktualizacja: {flow.lastModified}
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
          aria-label="Dodaj nowy Flow"
        >
          <PlusIcon className="h-5 w-5" />
          <span>Dodaj Flow</span>
        </Button>
      </div>
    </div>
  );
};

export default FlowPage;

// Ikona plusa dla przycisku
function PlusIcon({ className }) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      className={className}
    >
      <line x1="12" y1="5" x2="12" y2="19" />
      <line x1="5" y1="12" x2="19" y2="12" />
    </svg>
  );
}
