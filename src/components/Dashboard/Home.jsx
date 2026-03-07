import React, { useState } from 'react';
import { useAuth } from '../../context/AuthContext';

const Home = () => {
  const { user } = useAuth();
  const [searchKeyword, setSearchKeyword] = useState('');
  const [location, setLocation] = useState('Bangalore');
  const [experience, setExperience] = useState('2-5 yrs');
  const [feedback, setFeedback] = useState('');

  const handleSearch = () => {
    if (!searchKeyword.trim()) {
      setFeedback('Please enter a search keyword');
      setTimeout(() => setFeedback(''), 3000);
      return;
    }
    setFeedback(`🔎 Searching for "${searchKeyword}" in ${location} (${experience})`);
    setTimeout(() => setFeedback(''), 3000);
  };

  return (
    <>
      <div className="welcome-row">
        Welcome back, {user?.full_name || 'User'}! 👋
      </div>

      {feedback && <div className="feedback-message" style={{ marginBottom: '1rem' }}>{feedback}</div>}

      <div className="dashboard-grid">
        <div className="stat-panel">
          <div className="panel-header"><i className="fas fa-chart-pie"></i> 📊 Your Stats</div>
          <ul className="stats-list">
            <li><span>📌 Saved jobs</span> <span>12</span></li>
            <li><span>📤 Applied</span> <span>5</span></li>
            <li><span>🤝 Interviews</span> <span>2</span></li>
            <li><span>🎉 Offers</span> <span>0</span></li>
          </ul>
        </div>
        <div className="stat-panel">
          <div className="panel-header"><i className="fas fa-bullseye"></i> 🎯 Recommended Jobs</div>
          <ul className="rec-list">
            <li><i className="fab fa-python"></i> Python Developer <span className="match-badge">92% match</span></li>
            <li><i className="fas fa-chart-line"></i> Data Scientist <span className="match-badge">87% match</span></li>
            <li><i className="fab fa-aws"></i> Cloud Engineer <span className="match-badge">78% match</span></li>
          </ul>
        </div>
      </div>

      <div className="quick-search-panel">
        <div className="search-header"><i className="fas fa-magnifying-glass"></i> 🔍 Quick Job Search</div>
        <div className="search-row">
          <input 
            type="text" 
            className="search-input" 
            value={searchKeyword}
            onChange={(e) => setSearchKeyword(e.target.value)}
            placeholder="Job Title/Keywords"
          />
          <button className="search-btn" onClick={handleSearch}>
            <i className="fas fa-search"></i> 🔍
          </button>
        </div>
        <div className="filter-row">
          <div className="filter-item">
            📍 Location: 
            <select value={location} onChange={(e) => setLocation(e.target.value)}>
              <option>Bangalore</option>
              <option>Mumbai</option>
              <option>Delhi</option>
              <option>Pune</option>
              <option>Hyderabad</option>
              <option>Chennai</option>
            </select>
          </div>
          <div className="filter-item">
            📅 Exp: 
            <select value={experience} onChange={(e) => setExperience(e.target.value)}>
              <option>0-2 yrs</option>
              <option>2-5 yrs</option>
              <option>5-8 yrs</option>
              <option>8+ yrs</option>
            </select>
          </div>
        </div>
      </div>

      <div className="bottom-grid">
        <div className="stat-panel">
          <div className="panel-header"><i className="fas fa-clock"></i> 📌 Recent Activity</div>
          <ul className="activity-list">
            <li><i className="fas fa-bookmark"></i> Saved job at Microsoft <span style={{ color: '#7cabdf' }}>2h ago</span></li>
            <li><i className="fas fa-paper-plane"></i> Applied to Google <span style={{ color: '#7cabdf' }}>1d ago</span></li>
            <li><i className="fas fa-building"></i> Followed Amazon</li>
            <li><i className="fas fa-file-alt"></i> Updated resume</li>
            <li><i className="fas fa-chart-line"></i> Viewed job statistics</li>
          </ul>
        </div>
        <div className="stat-panel">
          <div className="panel-header"><i className="fas fa-calendar-alt"></i> 📅 Upcoming</div>
          <ul className="upcoming-list">
            <li><i className="fas fa-users"></i> Interview with Amazon <span className="match-badge">Tomorrow</span></li>
            <li><i className="fas fa-phone"></i> Follow-up with Google <span className="match-badge">Friday</span></li>
            <li><i className="fas fa-file-alt"></i> Resume review <span className="match-badge">Next week</span></li>
          </ul>
        </div>
      </div>
    </>
  );
};

export default Home;