import { useState } from "react";
import { useDispatch } from "react-redux";
import { editRating, createRating } from "../../store/sets";
import useSession from "../../hooks/useSession";
import { useModal } from "../../context/Modal";
import "./RatingForm.css";

export default function RatingForm({ rating, setId, ratingId }) {
  const [userRating, setUserRating] = useState(rating);
  let [currentRating, setCurrentRating] = useState(rating);
  const user = useSession();
  const { closeModal } = useModal();
  const dispatch = useDispatch();

  let displayStars = [];

  const mouseOverStar = (e) => {
    setCurrentRating(e.target.id);
  };

  const mouseLeftStar = (e) => {
    setCurrentRating(userRating);
  };

  const starClicker = (e) => {
    setUserRating(e.target.id);
    setCurrentRating(e.target.id);
  };

  const submitClicker = () => {
    if (rating === 0) {
      dispatch(
        createRating({
          userId: user.id,
          setId: setId,
          rating: userRating,
        })
      );
    } else {
      dispatch(
        editRating({
          id: ratingId,
          userId: user.id,
          setId: setId,
          rating: userRating,
        })
      );
    }
    closeModal();
  };

  for (let i = 1; i <= 5; i++) {
    if (i > currentRating) {
      displayStars.push(
        <i
          className="fa-regular fa-star"
          key={i}
          id={i}
          onMouseEnter={mouseOverStar}
          onMouseLeave={mouseLeftStar}
          onClick={starClicker}
        ></i>
      );
    } else {
      displayStars.push(
        <i
          id={i}
          className="fa-solid fa-star"
          style={{ color: "#A0B1FF" }}
          key={i}
          onMouseEnter={mouseOverStar}
          onMouseLeave={mouseLeftStar}
          onClick={starClicker}
        ></i>
      );
    }
  }
  return (
    <div className="RatingForm">
      <div className="RatingForm-title">How would you rate this set?</div>
      <div className="RatingForm-stars">{displayStars.map((star) => star)}</div>
      <div className="RatingForm-divider"></div>
      <div className="RatingForm-btn-wrapper">
        <button onClick={submitClicker}>Submit</button>
      </div>
    </div>
  );
}
