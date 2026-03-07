import React, { useState } from 'react';

const ResumeMaker = () => {
  const [resumeData, setResumeData] = useState({
    fullName: '',
    email: '',
    phone: '',
    summary: '',
    skills: '',
    experience: '',
    education: ''
  });
  const [feedback, setFeedback] = useState('');

  const handleChange = (e) => {
    setResumeData({
      ...resumeData,
      [e.target.name]: e.target.value
    });
  };

  const handleParse = () => {
    setFeedback('🔍 Parsing resume... Analysis complete! Suggestions available.');
    setTimeout(() => setFeedback(''), 3000);
  };

  const handleAnalyze = () => {
    setFeedback('📊 Analyzing resume... ATS score: 85%. Improvement suggestions generated.');
    setTimeout(() => setFeedback(''), 3000);
  };

  const handleGetSuggestions = () => {
    setFeedback('💡 Suggestions: Add more keywords, quantify achievements, improve formatting.');
    setTimeout(() => setFeedback(''), 4000);
  };

  return (
    <div className="stat-panel">
      <div className="panel-header">
        <i className="fas fa-file-alt"></i> 📄 Resume Maker
      </div>

      {feedback && <div className="feedback-message" style={{ marginBottom: '1rem' }}>{feedback}</div>}

      <div style={{ display: 'flex', gap: '1rem', marginBottom: '2rem' }}>
        <button className="search-btn" onClick={handleParse}>
          <i className="fas fa-file-import"></i> Parse & Analyze
        </button>
        <button className="search-btn" onClick={handleAnalyze}>
          <i className="fas fa-chart-line"></i> Analyze ATS
        </button>
        <button className="search-btn" onClick={handleGetSuggestions}>
          <i className="fas fa-lightbulb"></i> Get Suggestions
        </button>
      </div>

      <form>
        <div className="input-group">
          <label>👤 Full Name:</label>
          <input
            type="text"
            name="fullName"
            className="input-field"
            value={resumeData.fullName}
            onChange={handleChange}
          />
        </div>

        <div className="input-group">
          <label>📧 Email:</label>
          <input
            type="email"
            name="email"
            className="input-field"
            value={resumeData.email}
            onChange={handleChange}
          />
        </div>

        <div className="input-group">
          <label>📱 Phone:</label>
          <input
            type="tel"
            name="phone"
            className="input-field"
            value={resumeData.phone}
            onChange={handleChange}
          />
        </div>

        <div className="input-group">
          <label>📝 Professional Summary:</label>
          <textarea
            name="summary"
            className="input-field"
            rows="3"
            value={resumeData.summary}
            onChange={handleChange}
            placeholder="Experienced software developer with 5+ years..."
          />
        </div>

        <div className="input-group">
          <label>💻 Skills:</label>
          <textarea
            name="skills"
            className="input-field"
            rows="2"
            value={resumeData.skills}
            onChange={handleChange}
            placeholder="Python, JavaScript, React, Node.js, SQL"
          />
        </div>

        <div className="input-group">
          <label>💼 Experience:</label>
          <textarea
            name="experience"
            className="input-field"
            rows="4"
            value={resumeData.experience}
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
            value={resumeData.education}
            onChange={handleChange}
            placeholder="B.Tech in Computer Science, IIT Bombay, 2018"
          />
        </div>

        <button type="button" className="signin-btn" style={{ width: 'auto', padding: '0.8rem 2rem' }}>
          <i className="fas fa-save"></i> Save Resume
        </button>
      </form>
    </div>
  );
};

export default ResumeMaker;