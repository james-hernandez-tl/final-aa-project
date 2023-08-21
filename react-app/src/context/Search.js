import { createContext, useContext, useState } from "react";

const isSearchingContent = createContext(false);

export function IsSearchProvider({ children }) {
  const [isSearching, setIsSearching] = useState(true);

  return (
    <>
      <isSearchingContent.Provider value={{ isSearching, setIsSearching }}>
        {children}
      </isSearchingContent.Provider>
    </>
  );
}

export const useIsSearching = () => useContext(isSearchingContent);
