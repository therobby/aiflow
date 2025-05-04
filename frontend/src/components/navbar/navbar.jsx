"use client";

import {
  NavigationMenu,
  NavigationMenuList,
  NavigationMenuItem,
  NavigationMenuLink,
} from "@/components/ui/navigation-menu";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { ModeToggle } from "../theme/mode-toggle";

export default function Navbar() {
  const asPath = usePathname();

  const isActive = (path) => asPath === path;

  return (
    <div className="flex items-center justify-between max-w-full w-full p-5">
      <Link href="/" className="text-lg font-bold">
        AI Flow
      </Link>
      <NavigationMenu>
        <NavigationMenuList className="flex items-center max-w-full w-full">
          <NavigationMenuItem>
            <div className="flex space-x-4">
              <Link
                href="/flows"
                className={`text-lg hover:underline self-center ${
                  isActive("/flows") ? "font-bold text-blue-500" : ""
                }`}
              >
                Flows
              </Link>
              <Link
                href="/blocks"
                className={`text-lg hover:underline self-center ${
                  isActive("/blocks") ? "font-bold text-blue-500" : ""
                }`}
              >
                Blocks
              </Link>
              <ModeToggle />
            </div>
          </NavigationMenuItem>
        </NavigationMenuList>
      </NavigationMenu>
    </div>
  );
}
