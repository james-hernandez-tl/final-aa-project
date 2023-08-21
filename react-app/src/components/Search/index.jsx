import { useSearchParams } from "react-router-dom";
import SetMainLayout from "../SetMainLayout";
import useAllSets from "../../hooks/useAllSets";
import "./Search.css";
import { useEffect, useState } from "react";
import { searchSets } from "../../store/sets";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import ClipLoader from "react-spinners/ClipLoader";
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

  const loadingScreen = (
    <div className="Home-loadingScreen">
      <ClipLoader color="white" size={100} />
    </div>
  );

  if (!allSets) {
    return loadingScreen;
  }

  if (isSearching) return loadingScreen;

  allSets = Object.values(allSets);

  return (
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
        <div className="Search-preview">
          {/* <div className="Search-sets-title">Set preview</div> */}
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
              {previewSet &&
                Object.values(previewSet.Cards)
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
      </div>
    </div>
  );
}
