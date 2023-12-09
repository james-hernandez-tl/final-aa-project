import { createContext, useContext, useState } from "react";
export const ThemeContext = createContext(null);

export function useTheme() {
  return useContext(ThemeContext);
}

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState(localStorage.getItem("theme"));

  if (!theme) {
    localStorage.setItem("theme", "light");
    setTheme("light");
  }

  const toggleTheme = () => {
    if (theme === "light") {
      localStorage.setItem("theme", "dark");
      setTheme("dark");
    } else {
      localStorage.setItem("theme", "light");
      setTheme("light");
    }
  };

  return (
    <ThemeContext.Provider value={{ theme, setTheme, toggleTheme }}>
      <div id={theme}>{children}</div>
    </ThemeContext.Provider>
  );
}
