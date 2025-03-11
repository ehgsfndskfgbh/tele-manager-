import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { useEffect } from "react";

export default function TelegramChatManager() {
  const [accounts, setAccounts] = useState([]);
  const [selectedChat, setSelectedChat] = useState(null);
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState("");

  useEffect(() => {
    // Fetch accounts and messages from backend (placeholder logic)
  }, []);

  const handleSendMessage = () => {
    if (newMessage.trim() === "") return;
    
    // Send message via backend API (placeholder logic)
    setMessages([...messages, { text: newMessage, sender: "me" }]);
    setNewMessage("");
  };

  return (
    <div className="flex h-screen">
      {/* Sidebar for Accounts & Chats */}
      <div className="w-1/4 bg-gray-900 text-white p-4 overflow-y-auto">
        <h2 className="text-lg font-bold mb-4">Accounts</h2>
        {accounts.map((acc) => (
          <div key={acc.id} className="mb-2 p-2 bg-gray-800 rounded cursor-pointer">
            {acc.name}
          </div>
        ))}

        <h2 className="text-lg font-bold mt-6 mb-4">Chats</h2>
        {accounts.map((acc) => (
          acc.chats.map((chat) => (
            <div
              key={chat.id}
              className="mb-2 p-2 bg-gray-700 rounded cursor-pointer"
              onClick={() => setSelectedChat(chat)}
            >
              {chat.name} ({acc.name})
            </div>
          ))
        ))}
      </div>

      {/* Chat Window */}
      <div className="w-3/4 flex flex-col p-4">
        {selectedChat ? (
          <>
            <h2 className="text-lg font-bold mb-2">Chat with {selectedChat.name}</h2>
            <div className="flex-1 overflow-y-auto bg-gray-100 p-4 rounded-lg mb-4">
              {messages.map((msg, index) => (
                <div key={index} className={`mb-2 ${msg.sender === "me" ? "text-right" : "text-left"}`}>
                  <span className="inline-block bg-blue-500 text-white p-2 rounded-lg">
                    {msg.text}
                  </span>
                </div>
              ))}
            </div>
            <div className="flex">
              <Input
                className="flex-1 mr-2"
                value={newMessage}
                onChange={(e) => setNewMessage(e.target.value)}
                placeholder="Type a message..."
              />
              <Button onClick={handleSendMessage}>Send</Button>
            </div>
          </>
        ) : (
          <p>Select a chat to start messaging</p>
        )}
      </div>
    </div>
  );
}
