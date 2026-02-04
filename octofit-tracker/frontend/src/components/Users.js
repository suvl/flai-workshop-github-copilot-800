import React, { useState, useEffect } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [editingUser, setEditingUser] = useState(null);
  const [formData, setFormData] = useState({
    username: '',
    full_name: '',
    email: '',
    team: '',
    fitness_level: ''
  });
  const [updateMessage, setUpdateMessage] = useState(null);

  const fetchUsers = () => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
    console.log('Users - Fetching from REST API endpoint:', apiUrl);

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Users - Fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const usersData = data.results || data;
        console.log('Users - Processed data:', usersData);
        setUsers(Array.isArray(usersData) ? usersData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Users - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const handleEdit = (user) => {
    setEditingUser(user);
    setFormData({
      username: user.username || '',
      full_name: user.full_name || '',
      email: user.email || '',
      team: user.team || '',
      fitness_level: user.fitness_level || ''
    });
    setUpdateMessage(null);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/${editingUser.id}/`;
    
    fetch(apiUrl, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData)
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to update user');
        }
        return response.json();
      })
      .then(updatedUser => {
        console.log('User updated successfully:', updatedUser);
        setUpdateMessage({ type: 'success', text: 'User updated successfully!' });
        fetchUsers();
        setTimeout(() => {
          setEditingUser(null);
          setUpdateMessage(null);
        }, 1500);
      })
      .catch(error => {
        console.error('Error updating user:', error);
        setUpdateMessage({ type: 'error', text: 'Failed to update user. Please try again.' });
      });
  };

  const handleCancel = () => {
    setEditingUser(null);
    setUpdateMessage(null);
  };

  if (loading) return <div className="container mt-4"><div className="loading-spinner"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Loading...</span></div><p className="mt-2">Loading users...</p></div></div>;
  if (error) return <div className="container mt-4"><div className="error-message"><strong>Error:</strong> {error}</div></div>;

  return (
    <div className="container mt-4">
      <div className="page-header">
        <h2>👤 Users</h2>
      </div>
      <div className="table-container">
        <div className="table-responsive">
          <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>ID</th>
              <th>Username</th>
              <th>Full Name</th>
              <th>Email</th>
              <th>Team</th>
              <th>Fitness Level</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {users.length > 0 ? (
              users.map(user => (
                <tr key={user.id}>
                  <td>{user.id}</td>
                  <td><strong>{user.username}</strong></td>
                  <td>{user.full_name || '-'}</td>
                  <td>{user.email}</td>
                  <td>{user.team || '-'}</td>
                  <td><span className="badge bg-info">{user.fitness_level || 'Not set'}</span></td>
                  <td>
                    <button 
                      className="btn btn-primary btn-sm"
                      onClick={() => handleEdit(user)}
                    >
                      ✏️ Edit
                    </button>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="7" className="empty-state">No users found</td>
              </tr>
            )}
          </tbody>
        </table>
        </div>
      </div>

      {/* Edit User Modal */}
      {editingUser && (
        <div className="modal show d-block" style={{ backgroundColor: 'rgba(0,0,0,0.5)' }}>
          <div className="modal-dialog modal-dialog-centered">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Edit User: {editingUser.username}</h5>
                <button type="button" className="btn-close" onClick={handleCancel}></button>
              </div>
              <div className="modal-body">
                {updateMessage && (
                  <div className={`alert ${updateMessage.type === 'success' ? 'alert-success' : 'alert-danger'}`}>
                    {updateMessage.text}
                  </div>
                )}
                <form onSubmit={handleSubmit}>
                  <div className="mb-3">
                    <label className="form-label">Username</label>
                    <input
                      type="text"
                      className="form-control"
                      name="username"
                      value={formData.username}
                      onChange={handleInputChange}
                      required
                    />
                  </div>
                  <div className="mb-3">
                    <label className="form-label">Full Name</label>
                    <input
                      type="text"
                      className="form-control"
                      name="full_name"
                      value={formData.full_name}
                      onChange={handleInputChange}
                      required
                    />
                  </div>
                  <div className="mb-3">
                    <label className="form-label">Email</label>
                    <input
                      type="email"
                      className="form-control"
                      name="email"
                      value={formData.email}
                      onChange={handleInputChange}
                      required
                    />
                  </div>
                  <div className="mb-3">
                    <label className="form-label">Team</label>
                    <input
                      type="text"
                      className="form-control"
                      name="team"
                      value={formData.team}
                      onChange={handleInputChange}
                      placeholder="Enter team name"
                    />
                  </div>
                  <div className="mb-3">
                    <label className="form-label">Fitness Level</label>
                    <select
                      className="form-select"
                      name="fitness_level"
                      value={formData.fitness_level}
                      onChange={handleInputChange}
                    >
                      <option value="">Select fitness level</option>
                      <option value="Beginner">Beginner</option>
                      <option value="Intermediate">Intermediate</option>
                      <option value="Advanced">Advanced</option>
                      <option value="Expert">Expert</option>
                    </select>
                  </div>
                  <div className="modal-footer">
                    <button type="button" className="btn btn-secondary" onClick={handleCancel}>
                      Cancel
                    </button>
                    <button type="submit" className="btn btn-primary">
                      Save Changes
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Users;
