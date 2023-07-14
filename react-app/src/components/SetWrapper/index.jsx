import SetMainLayout from "../SetMainLayout";
import "./SetWrapper.css";

export default function SetWrapper({ allSets }) {
  return (
    <div className="SetWrapper">
      {allSets.map((set) => (
        <SetMainLayout set={set} key={set.id} />
      ))}
    </div>
  );
}
