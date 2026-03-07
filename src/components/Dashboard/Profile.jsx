import React, { useState, useEffect } from 'react';
import { useAuth } from '../../context/AuthContext';
import { userAPI } from '../../services/api';

const Profile = () => {
  const { user } = useAuth();
  const [profile, setProfile] = useState({
    full_name: '',
    email: '',
    phone: '',
    location: '',
    skills: '',
    experience: '',
    education: '',
    avatar: ''
  });
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState('');

  useEffect(() => {
    loadProfile();
  }, []);

  const loadProfile = async () => {
    try {
      const response = await userAPI.getProfile();
      setProfile(response.data);
    } catch (error) {
      setMessage('Failed to load profile');
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e) => {
    setProfile({
      ...profile,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSaving(true);
    setMessage('');

    try {
      await userAPI.updateProfile(profile);
      setMessage('✅ Profile updated successfully');
    } catch (error) {
      setMessage('❌ Failed to update profile');
    } finally {
      setSaving(false);
    }
  };

  if (loading) {
    return <div className="feedback-message">Loading profile...</div>;
  }

  return (
    <div className="stat-panel" style={{ maxWidth: '800px', margin: '0 auto' }}>
      <div className="panel-header">
        <i className="fas fa-id-card"></i> 👤 Profile Settings
      </div>

      {message && <div className="feedback-message" style={{ marginBottom: '1rem' }}>{message}</div>}

      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label>👤 Full Name:</label>
          <input
            type="text"
            name="full_name"
            className="input-field"
            value={profile.full_name || ''}
            onChange={handleChange}
            required
          />
        </div>

        <div className="input-group">
          <label>📧 Email:</label>
          <input
            type="email"
            name="email"
            className="input-field"
            value={profile.email || ''}
            onChange={handleChange}
            required
            disabled
          />
        </div>

        <div className="input-group">
          <label>📱 Phone:</label>
          <input
            type="tel"
            name="phone"
            className="input-field"
            value={profile.phone || ''}
            onChange={handleChange}
            placeholder="+91 98765 43210"
          />
        </div>

        <div className="input-group">
          <label>📍 Location:</label>
          <input
            type="text"
            name="location"
            className="input-field"
            value={profile.location || ''}
            onChange={handleChange}
            placeholder="Bangalore, India"
          />
        </div>

        <div className="input-group">
          <label>💻 Skills (comma separated):</label>
          <textarea
            name="skills"
            className="input-field"
            rows="3"
            value={profile.skills || ''}
            onChange={handleChange}
            placeholder="Python, JavaScript, React, SQL"
          />
        </div>

        <div className="input-group">
          <label>💼 Experience:</label>
          <textarea
            name="experience"
            className="input-field"
            rows="4"
            value={profile.experience || ''}
            onChange={handleChange}
            placeholder="Senior Developer at Google (2020-present)&#10;Software Engineer at Microsoft (2018-2020)"
          />
        </div>

        <div className="input-group">
          <label>🎓 Education:</label>
          <textarea
            name="education"
            className="input-field"
            rows="2"
            value={profile.education || ''}
            onChange={handleChange}
            placeholder="B.Tech in Computer Science, IIT Bombay, 2018"
          />
        </div>

        <button type="submit" className="signin-btn" disabled={saving}>
          <i className="fas fa-save"></i> {saving ? 'SAVING...' : 'SAVE PROFILE'}
        </button>
      </form>
    </div>
  );
};

export default Profile;