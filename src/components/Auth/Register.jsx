import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { authAPI } from '../../services/api';
import { GoogleLogin } from '@react-oauth/google';

const Register = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    fullName: '',
    email: '',
    password: '',
    confirmPassword: ''
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

    if (formData.password !== formData.confirmPassword) {
      setError('Passwords do not match');
      setLoading(false);
      return;
    }

    if (formData.password.length < 6) {
      setError('Password must be at least 6 characters');
      setLoading(false);
      return;
    }

    try {
      const response = await authAPI.register({
        full_name: formData.fullName,
        email: formData.email,
        password: formData.password
      });
      
      // Auto-login after registration
      localStorage.setItem('token', response.data.token);
      localStorage.setItem('user', JSON.stringify(response.data.user));
      navigate('/dashboard');
    } catch (err) {
      setError(err.response?.data?.message || 'Registration failed');
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleSuccess = async (credentialResponse) => {
    try {
      const response = await authAPI.googleAuth({
        tokenId: credentialResponse.credential
      });
      localStorage.setItem('token', response.data.token);
      localStorage.setItem('user', JSON.stringify(response.data.user));
      navigate('/dashboard');
    } catch (err) {
      setError('Google registration failed');
    }
  };

  return (
    <div className="auth-card">
      <div className="corner-marker"><span>+--------------------------------------------------+</span></div>
      <div className="title-bar" style={{ justifyContent: 'flex-start', gap: '8px' }}>
        <span className="mono-badge">⭐</span> Job Search AI Agent
      </div>
      <div className="login-box">
        <div className="lock-header">
          <div className="lock-icon"><i className="fas fa-pen-to-square"></i></div>
        </div>
        
        {error && <div className="feedback-message" style={{ color: '#f5b87b', marginBottom: '1rem' }}>{error}</div>}
        
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label>👤 Full Name:</label>
            <input 
              type="text" 
              className="input-field" 
              id="fullName" 
              placeholder="John Doe"
              value={formData.fullName}
              onChange={handleChange}
              required
            />
          </div>
          <div className="input-group">
            <label>📧 Email:</label>
            <input 
              type="email" 
              className="input-field" 
              id="email" 
              placeholder="john@example.com"
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
              minLength="6"
            />
          </div>
          <div className="input-group">
            <label>✓ Confirm Password:</label>
            <input 
              type="password" 
              className="input-field" 
              id="confirmPassword" 
              placeholder="··········" 
              value={formData.confirmPassword}
              onChange={handleChange}
              required
            />
          </div>
          <div className="checkbox-row">
            <input type="checkbox" id="termsCheck" defaultChecked required />
            <label htmlFor="termsCheck"> [✓] I agree to Terms & Conditions</label>
          </div>
          
          <button type="submit" className="signin-btn" disabled={loading}>
            <i className="fas fa-user-plus"></i> {loading ? 'REGISTERING...' : 'REGISTER'}
          </button>
        </form>

        <div style={{ textAlign: 'center', margin: '1rem 0', color: '#adccf0' }}>OR</div>

        <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '1.5rem' }}>
          <GoogleLogin
            onSuccess={handleGoogleSuccess}
            onError={() => setError('Google registration failed')}
            theme="filled_black"
            shape="pill"
            text="continue_with"
          />
        </div>

        <div className="register-link">
          <span>Already have an account?</span>
          <Link to="/login">Login</Link>
        </div>
      </div>
      <div className="corner-marker"><span>+--------------------------------------------------+</span></div>
    </div>
  );
};

export default Register;