import { useSearchParams } from "react-router-dom";
import SetMainLayout from "../SetMainLayout";
import useAllSets from "../../hooks/useAllSets";
import "./Search.css";
import { useEffect, useState } from "react";
import { searchSets } from "../../store/sets";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";

export default function Search() {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [searchParams, setSearchParams] = useSearchParams();
  const [previewSet, setPreviewSet] = useState(null);
  let allSets = useAllSets();
  const search = searchParams.get("search");

  const setClicker = () => {
    navigate(`/sets/${previewSet.id}`);
  };

  useEffect(() => {
    if (Array.isArray(allSets)) setPreviewSet(allSets[0]);
  }, [allSets]);

  useEffect(() => {
    dispatch(searchSets(`?search=${search}`));
  }, [searchParams]);

  if (!allSets) return null;

  allSets = Object.values(allSets);

  return (
    <div className="Search">
      <div className="Search-results">Results for "{search}"</div>
      <div className="Search-main-wrapper">
        <div className="Search-sets">
          <div className="Search-sets-title">Search Sets</div>
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
          <div className="Search-sets-title">Set preview</div>
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
