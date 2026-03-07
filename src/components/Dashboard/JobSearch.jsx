import React, { useState } from 'react';

const JobSearch = () => {
  const [jobs] = useState([
    { id: 1, title: 'Senior Python Developer', company: 'Google', location: 'Bangalore', match: 92, salary: '₹25-35L', type: 'Full-time' },
    { id: 2, title: 'Data Scientist', company: 'Amazon', location: 'Hyderabad', match: 87, salary: '₹20-30L', type: 'Full-time' },
    { id: 3, title: 'Frontend Engineer', company: 'Microsoft', location: 'Noida', match: 85, salary: '₹18-28L', type: 'Remote' },
    { id: 4, title: 'DevOps Engineer', company: 'Netflix', location: 'Mumbai', match: 79, salary: '₹30-45L', type: 'Full-time' },
    { id: 5, title: 'ML Engineer', company: 'Adobe', location: 'Bangalore', match: 88, salary: '₹22-35L', type: 'Hybrid' }
  ]);

  const [filters, setFilters] = useState({
    keyword: '',
    location: '',
    type: ''
  });

  const [savedJobs, setSavedJobs] = useState([]);
  const [feedback, setFeedback] = useState('');

  const handleFilterChange = (e) => {
    setFilters({
      ...filters,
      [e.target.name]: e.target.value
    });
  };

  const handleSaveJob = (job) => {
    if (!savedJobs.find(j => j.id === job.id)) {
      setSavedJobs([...savedJobs, job]);
      setFeedback(`✅ Job saved: ${job.title} at ${job.company}`);
    } else {
      setSavedJobs(savedJobs.filter(j => j.id !== job.id));
      setFeedback(`📌 Job removed: ${job.title}`);
    }
    setTimeout(() => setFeedback(''), 3000);
  };

  const filteredJobs = jobs.filter(job => {
    if (filters.keyword && !job.title.toLowerCase().includes(filters.keyword.toLowerCase())) return false;
    if (filters.location && job.location !== filters.location) return false;
    if (filters.type && job.type !== filters.type) return false;
    return true;
  });

  return (
    <div className="stat-panel">
      <div className="panel-header">
        <i className="fas fa-search"></i> 🔍 Job Search
      </div>

      {feedback && <div className="feedback-message" style={{ marginBottom: '1rem' }}>{feedback}</div>}

      <div className="filter-row" style={{ marginBottom: '2rem' }}>
        <div className="filter-item">
          <input
            type="text"
            name="keyword"
            className="search-input"
            placeholder="Search jobs..."
            value={filters.keyword}
            onChange={handleFilterChange}
            style={{ width: '200px' }}
          />
        </div>
        <div className="filter-item">
          📍 Location:
          <select name="location" value={filters.location} onChange={handleFilterChange}>
            <option value="">All</option>
            <option>Bangalore</option>
            <option>Mumbai</option>
            <option>Hyderabad</option>
            <option>Noida</option>
          </select>
        </div>
        <div className="filter-item">
          💼 Type:
          <select name="type" value={filters.type} onChange={handleFilterChange}>
            <option value="">All</option>
            <option>Full-time</option>
            <option>Remote</option>
            <option>Hybrid</option>
          </select>
        </div>
      </div>

      <div style={{ overflowX: 'auto' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ borderBottom: '2px solid #2f5577', color: '#adccf0' }}>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Job Title</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Company</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Location</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Match</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Salary</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Type</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Action</th>
            </tr>
          </thead>
          <tbody>
            {filteredJobs.map(job => (
              <tr key={job.id} style={{ borderBottom: '1px dotted #253e58' }}>
                <td style={{ padding: '0.8rem' }}>{job.title}</td>
                <td style={{ padding: '0.8rem' }}>{job.company}</td>
                <td style={{ padding: '0.8rem' }}>{job.location}</td>
                <td style={{ padding: '0.8rem' }}>
                  <span className="match-badge">{job.match}%</span>
                </td>
                <td style={{ padding: '0.8rem' }}>{job.salary}</td>
                <td style={{ padding: '0.8rem' }}>{job.type}</td>
                <td style={{ padding: '0.8rem' }}>
                  <button
                    onClick={() => handleSaveJob(job)}
                    style={{
                      background: savedJobs.find(j => j.id === job.id) ? '#f5b87b' : '#1e3d5e',
                      border: 'none',
                      borderRadius: '20px',
                      padding: '0.3rem 1rem',
                      color: 'white',
                      cursor: 'pointer'
                    }}
                  >
                    {savedJobs.find(j => j.id === job.id) ? '✓ Saved' : 'Save'}
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default JobSearch;