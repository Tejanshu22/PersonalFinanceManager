import brand from "../../config/brand.json";
import { Navigation } from "../components/Navigation";
import { GlobeStory } from "../components/GlobeStory";
import { MoneyFlows } from "../components/MoneyFlows";
import { SampleDashboard } from "../components/SampleDashboard";
import {
  ProductStory,
  Trust,
  Finale,
  Footer,
} from "../components/ProductStory";
export default function Home() {
  return (
    <>
      <a className="skip-link" href="#flow">
        Skip animated introduction
      </a>
      <Navigation brand={brand.display_name} />
      <main id="top">
        <GlobeStory brand={brand.display_name} />
        <MoneyFlows brand={brand.display_name} />
        <SampleDashboard brand={brand.display_name} />
        <ProductStory />
        <Trust />
        <Finale />
      </main>
      <Footer brand={brand.display_name} />
    </>
  );
}
