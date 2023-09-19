import YourItemLayout from "../YourItemLayout";

export default function Scrollable({ arr, isSet, searchTerm }) {
  return (
    <div>
      {arr.length
        ? arr.map((item) => (
            <YourItemLayout item={item} isSet={isSet} key={item.id} />
          ))
        : `No ${isSet ? "Sets" : "Folders"} matching ${searchTerm}`}
    </div>
  );
}
