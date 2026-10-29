import { createFileRoute } from "@tanstack/react-router";
import { useState, useEffect } from "react";
import { ArrowDown, ArrowUp, ArrowRight } from "lucide-react";
import { Button } from "@/components/ui/button";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "Artifact Grafx — Brand excavation for small businesses" },
      { name: "description", content: "We excavate, polish, and bring small-business brands online: identity, strategy, design, and marketing." },
      { property: "og:title", content: "Artifact Grafx — Brand excavation" },
      { property: "og:description", content: "Your brand is already in there. We dig it up and bring it online." },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
    ],
  }),
  component: Index,
});

const services = [
  ["01", "Brand Identity", "Your brand exists. We give it a face — logo, colors, and type that feel like you."],
  ["02", "Strategy", "A simple map for where you're going online. No 50-page decks, just direction."],
  ["03", "Design", "Websites, social graphics, and everything you need to show up well."],
  ["04", "Marketing", "Content and campaigns that reach the people who need you."],
];
const finds = [
  ["Specimen 001", "Riverside Bakery", "Identity + Web"],
  ["Specimen 002", "Kona Coffee Co.", "Packaging"],
  ["Specimen 003", "North Shore Yoga", "Social System"],
  ["Specimen 004", "Haus & Hearth", "Brand Strategy"],
  ["Specimen 005", "Tidewater Cycles", "Identity + Web"],
  ["Specimen 006", "Copper Kettle Diner", "Signage + Menu"],
  ["Specimen 007", "Marigold & Vine", "Packaging"],
  ["Specimen 008", "Foundry & Fern", "Brand Strategy"],
];

function Emblem() {
  return (
    <svg className="artifact-emblem" viewBox="0 0 64 88" role="img" aria-label="Artifact Grafx diamond emblem">
      <path d="M22 8 42 18M42 8 22 18M32 23 59 55 32 87 5 55Z" fill="none" stroke="currentColor" strokeWidth="2" />
      <text x="32" y="64" textAnchor="middle" fill="currentColor" fontFamily="sans-serif" fontSize="30">A</text>
    </svg>
  );
}
function Marker({ n, e, title }: { n: string; e: string; title: string }) {
  return (
    <div className="mb-10">
      <p className="label-mono mb-4 text-primary">N{n} | E{e}</p>
      <h2 className="text-3xl font-semibold md:text-4xl">{title}</h2>
    </div>
  );
}
function Index() {
  const [need, setNeed] = useState("Brand Identity");
  const [sent, setSent] = useState(false);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("active");
          }
        });
      },
      { threshold: 0.1, rootMargin: "0px 0px -50px 0px" }
    );

    document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));
    return () => observer.disconnect();
  }, []);

  return (
    <main id="top">
      <section className="artifact-opening flex flex-col items-center justify-center px-6 text-center">
        <div className="animate-rise flex flex-col items-center">
          <Emblem />
          <h1 className="mt-12 text-4xl font-bold sm:text-6xl">ArtifactGrafx</h1>
          <p className="mt-6 text-base leading-relaxed text-muted-foreground md:text-lg">
            <span className="text-primary">Artcheologist</span> — unearthing a creative presence online for small businesses
          </p>
          <p className="label-mono mt-4 text-primary/70 tracking-[0.3em]">Discover. Design. Deliver.</p>
          <Button asChild variant="link" className="label-mono mt-9 h-auto flex-col gap-2 text-primary/70 no-underline hover:text-primary hover:no-underline">
            <a href="#intro">Dig deeper<ArrowDown aria-hidden="true" /></a>
          </Button>
        </div>
      </section>

      <div className="mx-auto max-w-5xl px-6 md:px-10">
        <section id="intro" className="border-b py-16 text-center md:py-24 reveal">
          <p className="mx-auto max-w-2xl text-xl leading-relaxed text-muted-foreground md:text-2xl">
            <span className="text-foreground">Your business is real. Your brand? It's in there —</span><br className="hidden md:block" />
            {" "}buried under tech overwhelm and not knowing where to start.<br className="hidden md:block" />
            <span className="text-primary"> We excavate it. Polish it. Bring it online.</span>
          </p>
        </section>

        <section id="services" className="border-b py-16 md:py-24 reveal">
          <Marker n="03" e="07" title="What We Excavate" />
          <div className="grid gap-10 sm:grid-cols-2 lg:grid-cols-4">
            {services.map(([n, title, description], idx) => (
              <article key={title} className="border-t border-primary/40 pt-5 reveal" style={{ transitionDelay: `${idx * 100}ms` }}>
                <span className="label-mono text-primary/70">{n}</span>
                <h3 className="mt-3 text-xl font-semibold">{title}</h3>
                <p className="mt-3 text-sm leading-7 text-muted-foreground">{description}</p>
              </article>
            ))}
          </div>
        </section>

        <section id="finds" className="border-b py-16 md:py-24 reveal">
          <Marker n="05" e="14" title="Unearthed Artifacts" />
          <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
            {finds.map(([specimen, name, type], idx) => (
              <article key={specimen} className="flex aspect-[4/3] flex-col justify-between border bg-card/70 p-5 transition-all hover:border-primary/60 hover:-translate-y-1 reveal" style={{ transitionDelay: `${idx * 50}ms` }}>
                <span className="label-mono text-muted-foreground">{specimen}</span>
                <div><h3 className="text-lg font-medium">{name}</h3><p className="label-mono mt-2 text-primary">{type}</p></div>
              </article>
            ))}
          </div>
        </section>

        <section className="border-b py-16 md:py-24 reveal">
          <Marker n="07" e="21" title="The Artcheologist" />
          <div className="flex flex-col items-start gap-8 sm:flex-row sm:items-center">
            <div className="flex size-28 shrink-0 items-center justify-center border border-primary/40 bg-card font-display text-5xl text-primary">A</div>
            <p className="max-w-2xl text-lg leading-8 text-muted-foreground">
              Helps small businesses excavate their brand and bring it online. One conversation, one design, one launch at a time. No agency speak, no complicated process — just a steady hand and an eye for what makes you different.
            </p>
          </div>
        </section>

        <section id="dig" className="py-16 md:py-24 reveal">
          <Marker n="09" e="28" title="Start Your Dig" />
          <p className="text-muted-foreground">Not sure where to start? That's the whole point. Let's dig in.</p>
          {sent ? (
            <p role="status" className="mt-10 text-2xl text-primary">Thanks — we'll be in touch soon.</p>
          ) : (
            <form
              name="contact"
              method="POST"
              data-netlify="true"
              netlify-honeypot="bot-field"
              className="mt-10 grid max-w-2xl gap-6 sm:grid-cols-2"
              onSubmit={(event) => { event.preventDefault(); setSent(true); }}
            >
              <input type="hidden" name="form-name" value="contact" />
              <p className="hidden">
                <label>
                  Don't fill this out if you're human: <input name="bot-field" />
                </label>
              </p>
              <label className="flex flex-col gap-2 text-sm text-muted-foreground">Your name
                <input required name="name" autoComplete="name" placeholder="Your name" className="rounded-sm border bg-card px-4 py-3 text-foreground outline-none focus:border-primary" />
              </label>
              <label className="flex flex-col gap-2 text-sm text-muted-foreground">Email
                <input required name="email" type="email" autoComplete="email" placeholder="Email" className="rounded-sm border bg-card px-4 py-3 text-foreground outline-none focus:border-primary" />
              </label>
              <label className="flex flex-col gap-2 text-sm text-muted-foreground sm:col-span-2">What do you need?
                <select name="service" value={need} onChange={(event) => setNeed(event.target.value)} className="w-full rounded-sm border bg-card px-4 py-3 text-foreground outline-none focus:border-primary">
                  {["Brand Identity", "Website", "Social & Marketing", "Not sure — help me figure it out"].map((option) => <option key={option}>{option}</option>)}
                </select>
              </label>
              <Button type="submit" className="label-mono mt-2 h-12 justify-self-start rounded-sm px-8">Send <ArrowRight aria-hidden="true" /></Button>
            </form>
          )}
        </section>
        <footer className="flex flex-wrap items-center justify-between gap-4 border-t py-8">
          <div><p className="label-mono text-primary/70">N11 | E35</p><p className="mt-3 text-xs text-muted-foreground">© 2026 ArtifactGrafx</p></div>
          <Button asChild variant="ghost" size="icon" className="text-primary"><a href="#top" aria-label="Back to top"><ArrowUp /></a></Button>
        </footer>
      </div>
    </main>
  );
}
