import React, { useRef } from 'react';

export default function WebcamComponent() {
  const imgRef = useRef(null);

  return (
    <div>
      <img
        ref={imgRef}
        src="http://127.0.0.1:8000/video-feed/"
        alt="Live Stream"
        crossOrigin="anonymous"
        style={{ width: '100%' }}
      />
    </div>
  );
}
