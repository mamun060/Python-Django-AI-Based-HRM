import React, { useEffect, useState } from "react";

export default function TableComp() {
  const [attendanceData, setAttendanceData] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [nameFilter, setNameFilter] = useState("");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const rowsPerPage = 15;

useEffect(() => {
  const fetchData = () => {
    fetch("http://127.0.0.1:8000/attendance/")
      .then((res) => res.json())
      .then((data) => {
        if (Array.isArray(data)) {
          setAttendanceData(data);
        } else {
          console.warn("Unexpected API response:", data);
          setAttendanceData([]);
        }
      })
      .catch((err) => console.error("Failed to fetch attendance data:", err));
  };

  // Initial fetch
  fetchData();

  // Set interval to fetch every 5 seconds (adjust as needed)
  const intervalId = setInterval(fetchData, 1000);

  // Cleanup on unmount
  return () => clearInterval(intervalId);
}, []);

  // Filter logic
  const filteredData = attendanceData.filter((record) => {
    const matchName = nameFilter === "" || record.name.toLowerCase().includes(nameFilter.toLowerCase());
    const recordTime = new Date(record.time);
    const matchStart = startDate === "" || recordTime >= new Date(startDate);
    const matchEnd = endDate === "" || recordTime <= new Date(endDate + "T23:59:59");
    return matchName && matchStart && matchEnd;
  });

  // Pagination logic
  const totalPages = Math.ceil(filteredData.length / rowsPerPage) || 1;
  const startIndex = (currentPage - 1) * rowsPerPage;
  const currentData = filteredData.slice(startIndex, startIndex + rowsPerPage);

  const handlePrev = () => setCurrentPage((prev) => Math.max(prev - 1, 1));
  const handleNext = () => setCurrentPage((prev) => Math.min(prev + 1, totalPages));
  const handlePageClick = (pageNum) => setCurrentPage(pageNum);

  return (
    <>
      {/* Filter Inputs */}
      <div className="flex flex-wrap gap-4 mb-4">
        <input
          type="text"
          placeholder="Filter by Name"
          value={nameFilter}
          onChange={(e) => setNameFilter(e.target.value)}
          className="border p-2 rounded"
        />
        <input
          type="date"
          value={startDate}
          onChange={(e) => setStartDate(e.target.value)}
          className="border p-2 rounded"
        />
        <input
          type="date"
          value={endDate}
          onChange={(e) => setEndDate(e.target.value)}
          className="border p-2 rounded"
        />
      </div>

      {/* Table */}
      <div className="w-full overflow-x-auto">
        <table className="w-full text-left border border-collapse rounded sm:border-separate border-slate-200" cellSpacing="0">
          <thead>
            <tr>
              <th className="h-12 px-6 text-sm font-medium text-slate-700 bg-slate-100 border-l first:border-l-0">Name</th>
              <th className="h-12 px-6 text-sm font-medium text-slate-700 bg-slate-100 border-l first:border-l-0">Time</th>
              <th className="h-12 px-6 text-sm font-medium text-slate-700 bg-slate-100 border-l first:border-l-0">Accuracy</th>
              <th className="h-12 px-6 text-sm font-medium text-slate-700 bg-slate-100 border-l first:border-l-0">Image</th>
            </tr>
          </thead>
          <tbody>
            {currentData.length === 0 ? (
              <tr>
                <td colSpan="4" className="h-12 px-6 text-center text-sm text-slate-500">
                  No attendance data found.
                </td>
              </tr>
            ) : (
              currentData.map((record) => (
                <tr key={record.id}>
                  <td className="h-12 px-6 text-sm border-t border-l first:border-l-0 border-slate-200">{record.name}</td>
                  <td className="h-12 px-6 text-sm border-t border-l first:border-l-0 border-slate-200">
                    {new Date(record.time).toLocaleString()}
                  </td>
                  <td className="h-12 px-6 text-sm border-t border-l first:border-l-0 border-slate-200">
                    {(record.accuracy * 1).toFixed(2)}%
                  </td>
                  <td className="h-12 px-6 text-sm border-t border-l first:border-l-0 border-slate-200">
                    <img
                      src={`http://127.0.0.1:8000${record.image}`}
                      alt={`${record.name}'s attendance`}
                      className="h-12 w-12 object-cover rounded"
                    />
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>

      {/* Pagination Controls */}
      <div className="mt-4 flex justify-center items-center space-x-2">
        <button
          onClick={handlePrev}
          disabled={currentPage === 1}
          className={`px-3 py-1 border rounded ${
            currentPage === 1
              ? "text-gray-400 border-gray-300"
              : "text-blue-600 border-blue-600 hover:bg-blue-100"
          }`}
        >
          Prev
        </button>

        {[...Array(totalPages)].map((_, idx) => {
          const pageNum = idx + 1;
          return (
            <button
              key={pageNum}
              onClick={() => handlePageClick(pageNum)}
              className={`px-3 py-1 border rounded ${
                currentPage === pageNum
                  ? "bg-blue-600 text-white border-blue-600"
                  : "text-blue-600 border-blue-600 hover:bg-blue-100"
              }`}
            >
              {pageNum}
            </button>
          );
        })}

        <button
          onClick={handleNext}
          disabled={currentPage === totalPages}
          className={`px-3 py-1 border rounded ${
            currentPage === totalPages
              ? "text-gray-400 border-gray-300"
              : "text-blue-600 border-blue-600 hover:bg-blue-100"
          }`}
        >
          Next
        </button>
      </div>
    </>
  );
}
