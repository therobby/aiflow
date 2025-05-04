"use client";

import {
  NavigationMenu,
  NavigationMenuList,
  NavigationMenuItem,
  NavigationMenuLink,
} from "@/components/ui/navigation-menu";
import Link from "next/link";
import { useRouter } from "next/navigation";

export default function Navbar() {
  const { asPath } = useRouter();

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
                className={`text-lg hover:underline ${
                  isActive("/flows") ? "font-bold text-blue-500" : ""
                }`}
              >
                Flows
              </Link>
              <Link
                href="/blocks"
                className={`text-lg hover:underline ${
                  isActive("/blocks") ? "font-bold text-blue-500" : ""
                }`}
              >
                Blocks
              </Link>
            </div>
          </NavigationMenuItem>
        </NavigationMenuList>
      </NavigationMenu>
    </div>
  );
}
