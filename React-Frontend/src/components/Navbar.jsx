
import { useState } from 'react';
import FaceRecognition from './webcam';
import TableComp from './TableComp';
import { Menu, X, Filter } from 'lucide-react';
import image from '../assets/sfs.png';
import Card from './Card';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);


  return (
    <div className="flex flex-col h-screen">
      {/* Navbar */}
      <div className="bg-orange-500 text-white flex items-center justify-between px-4 py-2 shadow-md">
        <div className="flex items-center gap-4">
          <button className="md:hidden" onClick={() => setIsOpen(!isOpen)}>
            {isOpen ? <X /> : <Menu />}
          </button>
          HRM
        </div>
        
        </div>

      {/* Main Content */}
      <div className="p-7 flex-1 overflow-y-auto">
        <Card title="Live Camera Feed">
          <FaceRecognition />
        </Card>
        <TableComp/>
      </div>
    </div>
  );
};

export default Navbar;
