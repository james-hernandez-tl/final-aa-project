import { getOneSetThunk } from "../../store/sets";
import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import useSession from "../../hooks/useSession";
import { deleteSetThunk } from "../../store/sets";
import { useMenu } from "../Menu";
import { Menu, MenuItem } from "../Menu";
import AddSetToFolder from "../AddSetToFolder";
import RatingForm from "../RatingForm";
import { useModal } from "../../context/Modal";
import OptionsForSet from "../OptionsForSet";
import ClipLoader from "react-spinners/ClipLoader";
import MainCardView from "./MainCardView";
import "./SetSingleView.css";

export default function SetSingleView() {
  const { setModalContent } = useModal();
  const { btnRef, hideMenu, toggleMenu, show, menuRef } = useMenu();
  const navigate = useNavigate();
  const { setId } = useParams();
  const dispatch = useDispatch();
  const [isFlipped, setIsFlipped] = useState(false);
  const [index, setIndex] = useState(0);
  const [containerClassName, setContainerClassName] = useState("");

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
    setIndex((index) => (index < set.Cards.length - 1 ? index + 1 : index));
    setContainerClassName("move-right");
    setTimeout(() => {
      setContainerClassName("");
    }, 500);
  };

  const prevClicker = () => {
    setIndex((index) => (index > 0 ? index - 1 : index));
    setContainerClassName("move-left");
    setTimeout(() => {
      setContainerClassName("");
    }, 500);
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
      <MainCardView
        cards={set.Cards}
        isFlipped={isFlipped}
        setIsFlipped={setIsFlipped}
        index={index}
        setIndex={setIndex}
        containerClassName={containerClassName}
      />
      <div className="setSingleView-slider-controls">
        <div className="setSingleView-arrow-holders" onClick={prevClicker}>
          <i className="fa-solid fa-arrow-left"></i>
        </div>
        <div className="setSingleView-slider-controls-NumSets">
          {index + 1}/{set.Cards.length}
        </div>
        <div className="setSingleView-arrow-holders" onClick={nextClicker}>
          <i className="fa-solid fa-arrow-right"></i>
        </div>
      </div>
      <div className="SetSingleView-footer">
        <div
          className="SetSingleView-card-dropdown"
          ref={btnRef}
          onClick={toggleMenu}
        >
          <i className="fa-solid fa-ellipsis"></i>
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
