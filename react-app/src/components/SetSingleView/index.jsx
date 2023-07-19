import { getOneSetThunk } from "../../store/sets";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import useSession from "../../hooks/useSession";
import { deleteSetThunk } from "../../store/sets";
import { useRef } from "react";
import { useMenu } from "../Menu";
import { Menu, MenuItem } from "../Menu";
import "./SetSingleView.css";

export default function SetSingleView() {
  const { btnRef, hideMenu, toggleMenu, show, menuRef } = useMenu();
  const sliderRef = useRef(null);
  const navigate = useNavigate();
  const { setId } = useParams();
  const dispatch = useDispatch();

  const set = useSelector((state) => state.sets.singleSet);
  const user = useSession();

  useEffect(() => {
    dispatch(getOneSetThunk(setId));
  }, [dispatch, setId]);

  const editSetClicker = () => {
    navigate(`/sets/${setId}/edit`);
  };

  const deleteSetClicker = () => {
    dispatch(deleteSetThunk(setId));
    navigate("/sets");
  };

  const nextClicker = () => {
    const scrollDistance = sliderRef.current.offsetWidth;
    sliderRef.current.scrollBy({
      left: scrollDistance,
    });
  };

  const prevClicker = () => {
    const scrollDistance = sliderRef.current.offsetWidth;
    sliderRef.current.scrollBy({
      left: -scrollDistance,
    });
  };

  if (!set) return <div>There is no set with this id</div>;

  return (
    <div className="SetSingleView">
      <div className="SetSingleView-title">{set.name}</div>
      <div className="SetSingleView-rating">
        <div className="SetSingleView-rating-star">
          <i className="fa-regular fa-star"></i>
        </div>
        <div className="SetSingleView-rating-score">{set.Rating}</div>
        <div>({set.NumRatings} reviews)</div>
      </div>
      <div className="SetSingleView-slider" ref={sliderRef}>
        {set.Cards.slice(0, 3).map((card) => (
          <div key={card.id} className="SetSingleView-card">
            <div className="SetSingleView-card-header">
              <div className="SetSingleView-card-hint">Get a hint</div>
            </div>
            <div className="SetSingleView-card-content">{card.question}</div>
          </div>
        ))}
      </div>
      <div className="setSingleView-slider-controls">
        <div onClick={nextClicker}>Next</div>
        <div onClick={prevClicker}>Previous</div>
      </div>
      <div className="SetSingleView-footer">
        <div className="SetSingleView-card-dropdown">
          <i
            ref={btnRef}
            onClick={toggleMenu}
            className="fa-solid fa-ellipsis"
          ></i>
        </div>
        <Menu menuRef={menuRef} isOpen={show} right>
          <MenuItem
            text="New Set"
            onClick={() => {
              hideMenu();
            }}
          />
          {user?.id === set.userId && <MenuItem text="Edit Set" />}
          {user?.id === set.userId && <MenuItem text="Delete Set" />}
        </Menu>
      </div>
      {set.userId === user?.id && <div onClick={editSetClicker}>EDIT SET</div>}
      {set.userId === user?.id && (
        <div onClick={deleteSetClicker}>DELETE SET</div>
      )}
    </div>
  );
}
