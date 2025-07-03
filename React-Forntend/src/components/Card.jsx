import React from "react";

export default function Card({ title = "Webcam", icon, children }) {
  return (
    <div className="bg-white rounded-xl shadow-md text-slate-500 w-full max-w-md mx-auto overflow-hidden">
      <div className="p-2">
        <h3 className="text-lg font-semibold text-slate-700 mb-3">{title}</h3>
        {children}
      </div>
    </div>
  );
}
