import { getOneSetThunk } from "../../store/sets";
import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import useSession from "../../hooks/useSession";
import { deleteSetThunk } from "../../store/sets";
import { useRef } from "react";
import { useMenu } from "../Menu";
import { Menu, MenuItem } from "../Menu";
import AddSetToFolder from "../AddSetToFolder";
import RatingForm from "../RatingForm";
import { useModal } from "../../context/Modal";
import OptionsForSet from "../OptionsForSet";
import ClipLoader from "react-spinners/ClipLoader";
import "./SetSingleView.css";

export default function SetSingleView() {
  const { setModalContent } = useModal();
  const [showQuestion, setShowQuestion] = useState(true);
  const [numQuestion, setNumQuestion] = useState(1);
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
    if (numQuestion < set.Cards.length) setNumQuestion((state) => state + 1);
    setTimeout(() => {
      setShowQuestion(true);
    }, 300);
  };

  const prevClicker = () => {
    const scrollDistance = sliderRef.current.offsetWidth;
    sliderRef.current.scrollBy({
      left: -scrollDistance,
    });
    if (numQuestion > 1) setNumQuestion((state) => state - 1);
    setTimeout(() => {
      setShowQuestion(true);
    }, 300);
  };

  if (!set || set.id != setId)
    return (
      <div className="Home-loadingScreen">
        <ClipLoader color="white" size={100} />
      </div>
    );

  return (
    <div className="SetSingleView">
      <div className="SetSingleView-title">{set.name}</div>
      <div
        className="SetSingleView-rating"
        onClick={() => {
          setModalContent(
            <RatingForm
              rating={set.UserRating[0]}
              setId={set.id}
              ratingId={set.UserRating[1]}
            />
          );
        }}
      >
        <div className="SetSingleView-rating-star">
          <i className="fa-regular fa-star"></i>
        </div>
        <div className="SetSingleView-rating-score">{set.Rating}</div>
        <div>
          (
          {set.NumRatings === 1
            ? `${set.NumRatings} Review`
            : `${set.NumRatings} Reviews`}
          )
        </div>
      </div>
      <OptionsForSet setId={setId} />
      <div className="SetSingleView-slider" ref={sliderRef}>
        {set.Cards.map((card) => (
          <div key={card.id} className="SetSingleView-card">
            <div className="SetSingleView-card-header">
              <div className="SetSingleView-card-hint">
                {showQuestion ? (
                  <div>
                    {" "}
                    Get a hint <i className="fa-regular fa-lightbulb"></i>{" "}
                  </div>
                ) : (
                  ""
                )}
              </div>
            </div>
            <div
              className="SetSingleView-card-content"
              onClick={() => setShowQuestion((state) => !state)}
            >
              {showQuestion ? card.question : card.answer}
            </div>
          </div>
        ))}
      </div>
      <div className="setSingleView-slider-controls">
        <div className="setSingleView-arrow-holders" onClick={prevClicker}>
          <i className="fa-solid fa-arrow-left"></i>
        </div>
        <div className="setSingleView-slider-controls-NumSets">
          {numQuestion}/{set.Cards.length}
        </div>
        <div className="setSingleView-arrow-holders" onClick={nextClicker}>
          <i className="fa-solid fa-arrow-right"></i>
        </div>
      </div>
      <div className="SetSingleView-footer">
        <div className="SetSingleView-card-dropdown">
          <i
            ref={btnRef}
            onClick={toggleMenu}
            className="fa-solid fa-ellipsis"
          ></i>
        </div>
        <Menu
          menuRef={menuRef}
          isOpen={show}
          right
          top={user?.id === set.userId ? "-110px" : "-50px"}
        >
          <MenuItem
            text="Add set to folder"
            onClick={() => {
              hideMenu();
              setModalContent(<AddSetToFolder setId={set.id} />);
            }}
          />
          {user?.id === set.userId && (
            <MenuItem
              text="Edit Set"
              onClick={() => {
                hideMenu();
                editSetClicker();
              }}
            />
          )}
          {user?.id === set.userId && (
            <MenuItem
              text="Delete Set"
              onClick={() => {
                hideMenu();
                deleteSetClicker();
              }}
            />
          )}
        </Menu>
      </div>
    </div>
  );
}
