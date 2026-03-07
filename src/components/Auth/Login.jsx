import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import { authAPI } from '../../services/api';
import { GoogleLogin } from '@react-oauth/google';

const Login = () => {
  const navigate = useNavigate();
  const { login } = useAuth();
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.id]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const response = await authAPI.login(formData);
      login(response.data.token, response.data.user);
      navigate('/dashboard');
    } catch (err) {
      setError(err.response?.data?.message || 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleSuccess = async (credentialResponse) => {
    try {
      const response = await authAPI.googleAuth({
        tokenId: credentialResponse.credential
      });
      login(response.data.token, response.data.user);
      navigate('/dashboard');
    } catch (err) {
      setError('Google login failed');
    }
  };

  return (
    <div className="auth-card">
      <div className="corner-marker"><span>+--------------------------------------------------+</span></div>
      <div className="title-bar" style={{ justifyContent: 'flex-start', gap: '8px', borderBottom: 'none', marginBottom: '1rem' }}>
        <span className="mono-badge">⭐</span> Job Search AI Agent
      </div>
      <div className="login-box">
        <div className="lock-header">
          <div className="lock-icon"><i className="fas fa-lock"></i></div>
        </div>
        
        {error && <div className="feedback-message" style={{ color: '#f5b87b', marginBottom: '1rem' }}>{error}</div>}
        
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label>📧 Email:</label>
            <input 
              type="email" 
              className="input-field" 
              id="email" 
              placeholder="your.name@example.com" 
              value={formData.email}
              onChange={handleChange}
              required
            />
          </div>
          <div className="input-group">
            <label>🔒 Password:</label>
            <input 
              type="password" 
              className="input-field" 
              id="password" 
              placeholder="··········" 
              value={formData.password}
              onChange={handleChange}
              required
            />
          </div>
          <div className="checkbox-row">
            <input type="checkbox" id="loginRemember" defaultChecked />
            <label htmlFor="loginRemember"> [✓] Remember me</label>
            <span style={{ flex: 1, textAlign: 'right', opacity: 0.6 }}>⏎</span>
          </div>
          
          <button type="submit" className="signin-btn" disabled={loading}>
            <i className="fas fa-arrow-right-to-bracket"></i> {loading ? 'SIGNING IN...' : 'SIGN IN'}
          </button>
        </form>

        <div style={{ textAlign: 'center', margin: '1rem 0', color: '#adccf0' }}>OR</div>

        <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '1.5rem' }}>
          <GoogleLogin
            onSuccess={handleGoogleSuccess}
            onError={() => setError('Google login failed')}
            theme="filled_black"
            shape="pill"
            text="continue_with"
          />
        </div>

        <div className="register-link">
          <span>Don't have an account?</span>
          <Link to="/register">Register</Link>
          <span style={{ marginLeft: '8px' }}>⤻</span>
        </div>
      </div>
      <div className="corner-marker" style={{ marginTop: '1rem' }}>
        <span>+--------------------------------------------------+</span>
      </div>
      <div style={{ textAlign: 'right', fontSize: '0.7rem', opacity: 0.4, marginTop: '0.3rem' }}>
        🔐 secure · ai agent interface
      </div>
    </div>
  );
};

export default Login;