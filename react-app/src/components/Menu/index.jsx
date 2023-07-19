import { useRef, useState, useEffect } from "react";
import "./Menu.css";

export function Menu({ children, isOpen, menuRef, right, top = "45px" }) {
  if (!isOpen) return null;

  return (
    <div
      ref={menuRef}
      className="menu"
      style={{
        right: right ? 0 : undefined,
        top: top,
      }}
    >
      {children}
    </div>
  );
}

export function MenuItem({ icon, text, onClick }) {
  return (
    <div className="menu-item" onClick={onClick}>
      {icon}
      {text}
    </div>
  );
}

export function useMenu() {
  const [show, setShow] = useState(false);
  const btnRef = useRef(null);
  const menuRef = useRef(null);

  const toggleMenu = () => {
    setShow(!show);
  };

  const hideMenu = () => {
    setShow(false);
  };

  useEffect(() => {
    const closeMenu = (e) => {
      if (
        btnRef.current &&
        !btnRef.current.contains(e.target) &&
        menuRef.current &&
        !menuRef.current.contains(e.target)
      ) {
        setShow(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, []);

  return { btnRef, hideMenu, toggleMenu, show, menuRef };
}
