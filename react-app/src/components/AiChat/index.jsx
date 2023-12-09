import { useState, useEffect, useRef } from "react";
import { quizMe, chat, setMessages, teachMe } from "../../store/aiChat";
import { useDispatch } from "react-redux";
import { useParams } from "react-router-dom";
import { useSelector } from "react-redux";
import useSession from "../../hooks/useSession";
import Avatar from "../Avatar";
import PulseLoader from "react-spinners/PulseLoader";
import { useTheme } from "../../context/ColorProvider";
import "./AiChat.css";

export default function AiChat() {
  const { theme } = useTheme();
  const [userResponse, setUserResponse] = useState("");
  const dispatch = useDispatch();
  const { setId } = useParams();
  const allMessages = useSelector((state) => state.aiChat);
  const [isloading, setIsLoading] = useState(false);
  const [messageCount, setMessageCount] = useState(0);
  const user = useSession();
  const chatRef = useRef(null);
  const chatBoxRef = useRef(null);

  useEffect(() => {
    const inv = setInterval(() => {
      setMessageCount(0);
    }, 60000);

    return () => {
      clearInterval(inv);
    };
  }, []);

  useEffect(() => {
    let footer = document.getElementById("Footer");

    footer.classList.add("block-footer");
    return () => {
      footer.classList.remove("block-footer");
      dispatch(setMessages([]));
    };
  }, []);

  useEffect(() => {
    if (allMessages[allMessages.length - 1]?.content === "quiz me") {
      dispatch(quizMe(setId));
      setMessageCount((state) => state + 1);
      setIsLoading(true);
    } else if (allMessages[allMessages.length - 1]?.content === "Teach me") {
      dispatch(teachMe(setId));
      setMessageCount((state) => state + 1);
      setIsLoading(true);
    } else if (allMessages[allMessages.length - 1]?.role === "user") {
      dispatch(chat(allMessages));
      setMessageCount((state) => state + 1);
      setIsLoading(true);
    } else {
      setIsLoading(false);
    }
  }, [allMessages]);

  useEffect(() => {
    const lastChildElement = chatRef.current?.lastElementChild;
    lastChildElement?.scrollIntoView({ behavior: "smooth" });
  });

  const chatSubmit = () => {
    let messages = [...allMessages, { role: "user", content: userResponse }];
    dispatch(setMessages(messages));
  };

  // useEffect(() => {
  //   if (
  //     allMessages[allMessages.length - 1]?.content.includes("That's correct")
  //   ) {
  //     let messages = [
  //       ...allMessages,
  //       { role: "user", content: "What's my next question" },
  //     ];
  //     dispatch(chat(messages));
  //     setMessageCount((state) => state + 1);
  //   }
  // }, [allMessages]);

  useEffect(() => {
    chatBoxRef.current.innerHTML = "";
    let box = document.getElementsByClassName("AiChat-input");
    setTimeout(() => {
      box[0].focus();
    }, 200);
  }, [allMessages]);

  useEffect(() => {
    if (!isloading) {
      let box = document.getElementsByClassName("AiChat-input");
      setTimeout(() => {
        box[0].focus();
      }, 500);
    }
  }, [isloading]);

  return (
    <div className="AiChat">
      <div className="AiChat-allMessages" ref={chatRef}>
        <div className="AiChat-allMessages-message first-chat-message">
          <div className="AiChat-allMessages-message-icon"></div>
          <div className="AiChat-allMessages-message-text AiChat-allMessages-message-know">
            Hey there! KnowVerse is now using the power of AI to help you study
            more effectively. Let's get started!
          </div>
        </div>
        <div className="AiChat-allMessages-message">
          <div className="AiChat-allMessages-message-icon"></div>
          <div className="AiChat-allMessages-message-text AiChat-allMessages-message-know">
            Great! Looks like you're studying The Hedonic Calculus. Please
            select an activity.
          </div>
        </div>

        <div className="AiChat-allMessages-message">
          <div className="AiChat-allMessages-message-icon">
            {
              <Avatar
                size="35px"
                src={
                  "https://cdn.discordapp.com/attachments/934145502252003410/1153869569631473684/Screen_Shot_2023-09-19_at_9.45.26_PM.png"
                }
              />
            }
          </div>

          <div className="AiChat-allMessages-optionsBar">
            <div
              className="AiChat-allMessages-option"
              onClick={() => {
                dispatch(
                  setMessages([
                    ...allMessages,
                    { role: "user", content: "Teach me" },
                  ])
                );
              }}
            >
              <div className="AiChat-allMessages-option-icon">
                <i className="fa-solid fa-chalkboard-user"></i>
              </div>
              <div className="AiChat-allMessages-option-text">Teach me</div>
            </div>

            <div
              className="AiChat-allMessages-option"
              onClick={() => {
                dispatch(
                  setMessages([
                    ...allMessages,
                    { role: "user", content: "quiz me" },
                  ])
                );
              }}
            >
              <div className="OptionsForSet-option-icon">
                <i className="fa-solid fa-rectangle-list"></i>
              </div>
              <div className="OptionsForSet-option-text">Quiz me</div>
            </div>
          </div>
        </div>

        {allMessages.map((message, index) => {
          if (message.role === "system") return undefined;

          if (message.content === "What's my next question") return undefined;

          let isEnd =
            !allMessages[index + 1] ||
            allMessages[index + 1].role !== message.role;

          return (
            <div
              key={index}
              className={`AiChat-allMessages-message ${
                message.role === "user" ? "AiChat-allMessages-Usermessage" : ""
              }  ${isEnd ? "AiChat-allMessages-endMessage" : ""} `}
            >
              <div className="AiChat-allMessages-message-icon">
                {
                  <Avatar
                    src={
                      message.role === "user"
                        ? user?.image
                        : "https://cdn.discordapp.com/attachments/934145502252003410/1142924273611194428/Screen_Shot_2023-08-20_at_3.27.51_PM.png"
                    }
                    size="35px"
                  />
                }
              </div>
              <div className="AiChat-allMessages-message-text AiChat-allMessages-message-know">
                {message.content}
              </div>
            </div>
          );
        })}
        {isloading && (
          <div className="AiChat-allMessages-message AiChat-allMessages-loadingBubble-wrapper">
            <div className="AiChat-allMessages-message-icon">
              <Avatar
                size="35px"
                src={
                  "https://cdn.discordapp.com/attachments/934145502252003410/1153869569631473684/Screen_Shot_2023-09-19_at_9.45.26_PM.png"
                }
              />
            </div>
            <div className="AiChat-allMessages-message-loadingBubble">
              <PulseLoader
                speedMultiplier={0.8}
                loading={true}
                size={6}
                aria-label="Loading Spinner"
                data-testid="loader"
                color={theme === "light" ? "rgb(70, 70, 70)" : "#ffffff"}
              />
            </div>
          </div>
        )}
      </div>
      <div
        className={`AiChat-textBar ${
          messageCount < 3 && !isloading && allMessages.length
            ? ""
            : "AiChat-textBar-disabled"
        }`}
      >
        <div
          ref={chatBoxRef}
          contentEditable={
            messageCount < 3 && !isloading && allMessages.length
              ? "true"
              : "false"
          }
          data-placeholder="Do not enter any personal information"
          onInput={(e) => setUserResponse(e.currentTarget.textContent)}
          className="AiChat-input"
          onKeyPress={(e) => {
            if (e.key === "Enter") {
              chatSubmit();
              e.currentTarget.innerHTML = "";
              setUserResponse("");
            } else if (userResponse.length >= 300) {
              e.preventDefault();
            }
          }}
        ></div>

        <div className="AiChat-textBar-nav">{userResponse.length}/300</div>
      </div>
    </div>
  );
}
