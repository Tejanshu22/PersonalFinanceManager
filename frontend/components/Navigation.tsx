"use client";
import { useEffect, useRef, useState } from "react";
export function Navigation({ brand }: { brand: string }) {
  const [open, setOpen] = useState(false);
  const button = useRef<HTMLButtonElement>(null);
  useEffect(() => {
    const close = (event: KeyboardEvent) => {
      if (event.key === "Escape" && open) {
        setOpen(false);
        button.current?.focus();
      }
    };
    window.addEventListener("keydown", close);
    return () => window.removeEventListener("keydown", close);
  }, [open]);
  return (
    <header id="nav">
      <a href="#top" className="brand" aria-label={`${brand}, back to top`}>
        <span className="brandmark" aria-hidden="true">
          <span />
        </span>
        {brand}
      </a>
      <nav
        className={`navlinks${open ? " open" : ""}`}
        id="navlinks"
        aria-label="Main navigation"
      >
        {[
          ["top", "Discover"],
          ["flow", "Money flows"],
          ["demo", "Try the demo"],
          ["how", "How it works"],
          ["trust", "Trust"],
        ].map(([id, label]) => (
          <a key={id} href={`#${id}`} onClick={() => setOpen(false)}>
            {label}
          </a>
        ))}
      </nav>
      <a href="#demo" className="navbtn">
        Explore demo <span aria-hidden="true">↗</span>
      </a>
      <button
        ref={button}
        className="menu-btn"
        aria-controls="navlinks"
        aria-expanded={open}
        aria-label={open ? "Close navigation" : "Open navigation"}
        id="menu"
        onClick={() => setOpen(!open)}
      >
        {open ? "✕" : "☰"}
      </button>
    </header>
  );
}
