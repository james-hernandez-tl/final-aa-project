import YourItemLayout from "../YourItemLayout";

export default function Scrollable({ arr, isSet }) {
  return (
    <div>
      {arr.map((item) => (
        <YourItemLayout item={item} isSet={isSet} key={item.id} />
      ))}
    </div>
  );
}
