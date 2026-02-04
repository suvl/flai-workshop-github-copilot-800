import React, { useState, useEffect } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
    console.log('Leaderboard - Fetching from REST API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Leaderboard - Processed data:', leaderboardData);
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Leaderboard - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="container mt-4"><div className="loading-spinner"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Loading...</span></div><p className="mt-2">Loading leaderboard...</p></div></div>;
  if (error) return <div className="container mt-4"><div className="error-message"><strong>Error:</strong> {error}</div></div>;

  return (
    <div className="container mt-4">
      <div className="page-header">
        <h2>🏆 Leaderboard</h2>
      </div>
      <div className="table-container">
        <div className="table-responsive">
          <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>Rank</th>
              <th>User</th>
              <th>Team</th>
              <th>Total Calories</th>
              <th>Total Activities</th>
              <th>Total Points</th>
              <th>Duration (min)</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.length > 0 ? (
              leaderboard.map((entry, index) => (
                <tr key={entry.id || index}>
                  <td><strong>#{entry.rank || (index + 1)}</strong></td>
                  <td>
                    <strong>{entry.full_name || entry.username}</strong>
                    <br />
                    <small className="text-muted">@{entry.username}</small>
                  </td>
                  <td><span className="badge bg-info">{entry.team || 'N/A'}</span></td>
                  <td><span className="badge bg-success">{entry.total_calories || 0}</span></td>
                  <td>{entry.total_activities || 0}</td>
                  <td><span className="badge bg-primary">{entry.total_points || 0}</span></td>
                  <td>{entry.total_duration_minutes || 0}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="7" className="empty-state">No leaderboard data available</td>
              </tr>
            )}
          </tbody>
        </table>
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
