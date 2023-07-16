import SetMainLayout from "../SetMainLayout";
import "./SetWrapper.css";

export default function SetWrapper({ allSets, color = "#586380" }) {
  return (
    <div className="SetWrapper" style={{ background: color }}>
      <div className="slider">
        {allSets.map((set) => (
          <SetMainLayout set={set} key={set.id} />
        ))}
      </div>
    </div>
  );
}
