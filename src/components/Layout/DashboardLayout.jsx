import React from 'react';
import { Outlet, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';

const DashboardLayout = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { user, logout } = useAuth();

  const navItems = [
    { id: 'home', icon: 'fas fa-home', label: 'Home', path: '/dashboard' },
    { id: 'jobs', icon: 'fas fa-briefcase', label: 'Job Search', path: '/dashboard/jobs' },
    { id: 'resume', icon: 'fas fa-file-alt', label: 'Resume Maker', path: '/dashboard/resume' },
    { id: 'companies', icon: 'fas fa-building', label: 'Company Research', path: '/dashboard/companies' },
    { id: 'apps', icon: 'fas fa-clipboard-list', label: 'My Applications', path: '/dashboard/applications' },
    { id: 'profile', icon: 'fas fa-id-card', label: 'Profile', path: '/dashboard/profile' }
  ];

  return (
    <div className="dashboard-card">
      <div className="corner-marker"><span>+--------------------------------------------------+</span></div>
      
      <div className="title-bar">
        <div className="title-left">
          <i className="fas fa-star"></i> Job Search AI Agent
        </div>
        <div className="user-controls">
          <div className="user-badge">
            <i className="fas fa-user-circle"></i> 
            <span>{user?.full_name || 'User'}</span>
          </div>
          <div className="logout-btn" onClick={logout}>
            <i className="fas fa-sign-out-alt"></i> Logout
          </div>
        </div>
      </div>

      <div className="nav-menu">
        {navItems.map(item => (
          <button 
            key={item.id}
            className={`nav-item ${location.pathname === item.path ? 'active' : ''}`}
            onClick={() => navigate(item.path)}
          >
            <i className={item.icon}></i> {item.label}
          </button>
        ))}
      </div>

      <Outlet />

      <div className="corner-marker" style={{ marginTop: '1rem' }}>
        <span>+--------------------------------------------------+</span>
      </div>
      <div style={{ textAlign: 'right', fontSize: '0.7rem', opacity: 0.4, marginTop: '0.3rem' }}>
        🔐 ai agent · secure dashboard
      </div>
    </div>
  );
};

export default DashboardLayout;