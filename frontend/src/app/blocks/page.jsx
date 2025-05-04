import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Plus } from "lucide-react";

const BlocksPage = () => {
  const sampleBlocks = [
    {
      id: 1,
      name: "Scrap Web Page",
      description: "Get data from web page as json",
      status: "active",
      lastModified: "2024-03-20",
    },
    {
      id: 2,
      name: "Image Recognition",
      description: "Get image content using AI",
      status: "inactive",
      lastModified: "2024-02-01",
    },
    {
      id: 3,
      name: "Get last sales statistics",
      description: "Get last sales stats from api",
      status: "active",
      lastModified: "2024-05-18",
    },
  ];

  return (
    <div className="flex flex-col items-center min-h-screen p-4">
      <div className="w-full max-w-6xl">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {sampleBlocks.map((block) => (
            <Card key={block.id} className="h-full flex flex-col">
              <CardHeader>
                <CardTitle className="text-lg font-semibold">
                  {block.name}
                </CardTitle>
                <CardDescription className="text-sm text-muted-foreground">
                  {block.description}
                </CardDescription>
              </CardHeader>
              <div className="flex items-center justify-between p-4">
                <span
                  className={`text-sm font-medium ${
                    block.status === "active"
                      ? "text-green-600"
                      : "text-gray-500"
                  }`}
                >
                  Status: {block.status}
                </span>
                <span className="text-xs text-muted-foreground">
                  Last update: {block.lastModified}
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
          aria-label="Add new Block"
        >
          <Plus className="h-5 w-5" />
          <span>Add Blocks</span>
        </Button>
      </div>
    </div>
  );
};

export default BlocksPage;
