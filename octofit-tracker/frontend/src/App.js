import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              <img src="/octofitapp-logo.png" alt="OctoFit Logo" className="navbar-logo" />
              OctoFit Tracker
            </Link>
            <button 
              className="navbar-toggler" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#navbarNav"
              aria-controls="navbarNav" 
              aria-expanded="false" 
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Workout Suggestions</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <div className="main-content">
          <Routes>
            <Route path="/" element={
              <div className="container">
                <div className="welcome-section text-center">
                  <h1 className="display-4">Welcome to OctoFit Tracker</h1>
                  <p className="lead">Track your fitness activities, compete with teams, and achieve your goals!</p>
                  <hr className="my-4" style={{borderColor: 'rgba(255,255,255,0.3)'}} />
                  <p className="mb-0">Choose a section below to get started</p>
                </div>
                
                <div className="row mt-5">
                  <div className="col-md-6 col-lg-3 mb-4">
                    <Link to="/users" className="text-decoration-none">
                      <div className="card text-center h-100 home-card">
                        <div className="card-body d-flex flex-column justify-content-center">
                          <div className="display-1 mb-3">👤</div>
                          <h3 className="card-title">Users</h3>
                          <p className="card-text text-muted">Manage user profiles and team assignments</p>
                        </div>
                      </div>
                    </Link>
                  </div>
                  
                  <div className="col-md-6 col-lg-3 mb-4">
                    <Link to="/activities" className="text-decoration-none">
                      <div className="card text-center h-100 home-card">
                        <div className="card-body d-flex flex-column justify-content-center">
                          <div className="display-1 mb-3">🏃</div>
                          <h3 className="card-title">Activities</h3>
                          <p className="card-text text-muted">View and track fitness activities</p>
                        </div>
                      </div>
                    </Link>
                  </div>
                  
                  <div className="col-md-6 col-lg-3 mb-4">
                    <Link to="/teams" className="text-decoration-none">
                      <div className="card text-center h-100 home-card">
                        <div className="card-body d-flex flex-column justify-content-center">
                          <div className="display-1 mb-3">👥</div>
                          <h3 className="card-title">Teams</h3>
                          <p className="card-text text-muted">Explore teams and their members</p>
                        </div>
                      </div>
                    </Link>
                  </div>
                  
                  <div className="col-md-6 col-lg-3 mb-4">
                    <Link to="/leaderboard" className="text-decoration-none">
                      <div className="card text-center h-100 home-card">
                        <div className="card-body d-flex flex-column justify-content-center">
                          <div className="display-1 mb-3">🏆</div>
                          <h3 className="card-title">Leaderboard</h3>
                          <p className="card-text text-muted">See who's leading the competition</p>
                        </div>
                      </div>
                    </Link>
                  </div>
                  
                  <div className="col-md-6 col-lg-3 mb-4">
                    <Link to="/workouts" className="text-decoration-none">
                      <div className="card text-center h-100 home-card">
                        <div className="card-body d-flex flex-column justify-content-center">
                          <div className="display-1 mb-3">💪</div>
                          <h3 className="card-title">Workouts</h3>
                          <p className="card-text text-muted">Get personalized workout suggestions</p>
                        </div>
                      </div>
                    </Link>
                  </div>
                </div>
              </div>
            } />
            <Route path="/users" element={<Users />} />
            <Route path="/activities" element={<Activities />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/workouts" element={<Workouts />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
