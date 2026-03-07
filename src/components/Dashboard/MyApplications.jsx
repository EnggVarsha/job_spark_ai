import React, { useState } from 'react';

const MyApplications = () => {
  const [applications, setApplications] = useState([
    { id: 1, company: 'Google', position: 'Senior Python Developer', applied: '2024-01-15', status: 'Applied', notes: 'Waiting for response' },
    { id: 2, company: 'Amazon', position: 'Data Scientist', applied: '2024-01-10', status: 'Interview', notes: 'Interview scheduled for tomorrow' },
    { id: 3, company: 'Microsoft', position: 'Frontend Engineer', applied: '2024-01-05', status: 'Reviewed', notes: 'Technical test sent' },
    { id: 4, company: 'Netflix', position: 'DevOps Engineer', applied: '2024-01-01', status: 'Rejected', notes: 'Not selected' },
    { id: 5, company: 'Adobe', position: 'ML Engineer', applied: '2024-01-12', status: 'Offer', notes: 'Offer received!' }
  ]);

  const [selectedApp, setSelectedApp] = useState(null);
  const [noteText, setNoteText] = useState('');
  const [statusFilter, setStatusFilter] = useState('All');
  const [feedback, setFeedback] = useState('');

  const statuses = ['All', 'Applied', 'Reviewed', 'Interview', 'Offer', 'Rejected'];

  const handleStatusChange = (id, newStatus) => {
    setApplications(applications.map(app =>
      app.id === id ? { ...app, status: newStatus } : app
    ));
    setFeedback(`✅ Status updated to ${newStatus}`);
    setTimeout(() => setFeedback(''), 3000);
  };

  const handleAddNote = (id) => {
    if (!noteText.trim()) return;
    setApplications(applications.map(app =>
      app.id === id ? { ...app, notes: noteText } : app
    ));
    setNoteText('');
    setSelectedApp(null);
    setFeedback('📝 Note added successfully');
    setTimeout(() => setFeedback(''), 3000);
  };

  const handleTrackProgress = (id) => {
    setFeedback(`📊 Tracking progress for application #${id}`);
    setTimeout(() => setFeedback(''), 3000);
  };

  const filteredApps = statusFilter === 'All' 
    ? applications 
    : applications.filter(app => app.status === statusFilter);

  return (
    <div className="stat-panel">
      <div className="panel-header">
        <i className="fas fa-clipboard-list"></i> 📋 My Applications
      </div>

      {feedback && <div className="feedback-message" style={{ marginBottom: '1rem' }}>{feedback}</div>}

      <div className="filter-row" style={{ marginBottom: '2rem' }}>
        <div className="filter-item">
          📊 Filter by Status:
          <select value={statusFilter} onChange={(e) => setStatusFilter(e.target.value)}>
            {statuses.map(status => (
              <option key={status} value={status}>{status}</option>
            ))}
          </select>
        </div>
      </div>

      <div style={{ overflowX: 'auto' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ borderBottom: '2px solid #2f5577', color: '#adccf0' }}>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Company</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Position</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Applied Date</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Status</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Notes</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Actions</th>
            </tr>
          </thead>
          <tbody>
            {filteredApps.map(app => (
              <tr key={app.id} style={{ borderBottom: '1px dotted #253e58' }}>
                <td style={{ padding: '0.8rem' }}>{app.company}</td>
                <td style={{ padding: '0.8rem' }}>{app.position}</td>
                <td style={{ padding: '0.8rem' }}>{app.applied}</td>
                <td style={{ padding: '0.8rem' }}>
                  <select
                    value={app.status}
                    onChange={(e) => handleStatusChange(app.id, e.target.value)}
                    style={{
                      background: '#102433',
                      border: '2px solid #264b6b',
                      borderRadius: '20px',
                      padding: '0.3rem',
                      color: '#e8f0fe'
                    }}
                  >
                    {statuses.filter(s => s !== 'All').map(status => (
                      <option key={status} value={status}>{status}</option>
                    ))}
                  </select>
                </td>
                <td style={{ padding: '0.8rem' }}>{app.notes}</td>
                <td style={{ padding: '0.8rem' }}>
                  <button
                    onClick={() => setSelectedApp(app)}
                    style={{
                      background: '#1e3d5e',
                      border: 'none',
                      borderRadius: '20px',
                      padding: '0.3rem 1rem',
                      color: 'white',
                      cursor: 'pointer',
                      marginRight: '0.5rem'
                    }}
                  >
                    <i className="fas fa-pen"></i> Add Note
                  </button>
                  <button
                    onClick={() => handleTrackProgress(app.id)}
                    style={{
                      background: '#2d4b6e',
                      border: 'none',
                      borderRadius: '20px',
                      padding: '0.3rem 1rem',
                      color: 'white',
                      cursor: 'pointer'
                    }}
                  >
                    <i className="fas fa-chart-line"></i> Track
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {selectedApp && (
        <div className="stat-panel" style={{ marginTop: '2rem' }}>
          <div className="panel-header">
            <i className="fas fa-pen"></i> Add Note for {selectedApp.position} at {selectedApp.company}
          </div>
          <textarea
            className="input-field"
            rows="3"
            value={noteText}
            onChange={(e) => setNoteText(e.target.value)}
            placeholder="Enter your notes..."
          />
          <div style={{ display: 'flex', gap: '1rem', marginTop: '1rem' }}>
            <button
              className="search-btn"
              onClick={() => handleAddNote(selectedApp.id)}
            >
              Save Note
            </button>
            <button
              className="search-btn"
              style={{ background: '#2d4b6e' }}
              onClick={() => setSelectedApp(null)}
            >
              Cancel
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default MyApplications;