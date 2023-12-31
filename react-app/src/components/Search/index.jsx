import { useSearchParams } from "react-router-dom";
import SetMainLayout from "../SetMainLayout";
import useAllSets from "../../hooks/useAllSets";
import "./Search.css";
import { useEffect, useState } from "react";
import { searchSets } from "../../store/sets";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import LoadingScreen from "../LoadingScreen";
import { useIsSearching } from "../../context/Search";

export default function Search() {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [searchParams, setSearchParams] = useSearchParams();
  const [previewSet, setPreviewSet] = useState(null);
  let allSets = useAllSets();
  const search = searchParams.get("search");
  const { isSearching, setIsSearching } = useIsSearching();

  const setClicker = () => {
    if (previewSet) navigate(`/sets/${previewSet.id}`);
  };

  useEffect(() => {
    if (Array.isArray(allSets)) setPreviewSet(allSets[0]);
  }, [allSets]);

  useEffect(() => {
    async function stuff() {
      await dispatch(searchSets(`?search=${search}`));
      setIsSearching(false);
    }
    stuff();
  }, [searchParams]);

  if (!allSets) {
    return <LoadingScreen />;
  }
  allSets = Object.values(allSets);

  if (isSearching) return <LoadingScreen />;

  return (
    <div className="Search-wrapper">
      <div className="Search">
        <div className="Search-results">
          {allSets.length
            ? `Results for "${search}"`
            : `No results for "${search}"`}{" "}
        </div>
        <div className="Search-sets-title-wrapper">
          <div className="Search-sets-title">Search Sets</div>
          <div className="Search-sets-title search-preview-title">
            Set preview
          </div>
        </div>
        <div className="Search-main-wrapper">
          <div className="Search-sets">
            {/* <div className="Search-sets-title">Search Sets</div> */}
            {allSets.map((set) => (
              <SetMainLayout
                key={set.id}
                set={set}
                inSearch
                setPreviewSet={setPreviewSet}
              />
            ))}
          </div>
          {previewSet && (
            <div className="Search-preview">
              <div className="Search-prebiew-body">
                <div className="Search-prebiew-body-header">
                  <div className="Search-prebiew-body-title">
                    {previewSet?.name}
                  </div>
                  <div className="Search-prebiew-body-study">
                    <button onClick={setClicker}>Study</button>
                  </div>
                </div>
                <div>
                  {Object.values(previewSet.Cards)
                    .slice(0, 7)
                    .map((card) => (
                      <div key={card.id}>
                        <div className="Search-preview-body-question">
                          {card.question}
                        </div>
                        <div className="Search-preview-body-answer">
                          {card.answer}
                        </div>
                      </div>
                    ))}
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
