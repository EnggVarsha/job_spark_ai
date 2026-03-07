import React, { useState } from 'react';

const CompanyResearch = () => {
  const [companies] = useState([
    { id: 1, name: 'Google', rating: 4.5, reviews: 15234, culture: 'Excellent', salary: 'High', growth: 'Good' },
    { id: 2, name: 'Microsoft', rating: 4.3, reviews: 12456, culture: 'Good', salary: 'High', growth: 'Excellent' },
    { id: 3, name: 'Amazon', rating: 4.0, reviews: 21345, culture: 'Fast-paced', salary: 'Competitive', growth: 'Excellent' },
    { id: 4, name: 'Meta', rating: 4.2, reviews: 9876, culture: 'Innovative', salary: 'Very High', growth: 'Good' },
    { id: 5, name: 'Apple', rating: 4.4, reviews: 11345, culture: 'Excellent', salary: 'High', growth: 'Good' }
  ]);

  const [selectedCompany, setSelectedCompany] = useState(null);
  const [feedback, setFeedback] = useState('');

  const handleViewReviews = (company) => {
    setFeedback(`📊 Showing ${company.reviews} reviews for ${company.name}`);
    setTimeout(() => setFeedback(''), 3000);
  };

  const handleCompare = (company1, company2) => {
    setFeedback(`📊 Comparing ${company1.name} with ${company2.name}`);
    setTimeout(() => setFeedback(''), 3000);
  };

  return (
    <div className="stat-panel">
      <div className="panel-header">
        <i className="fas fa-building"></i> 🏢 Company Research
      </div>

      {feedback && <div className="feedback-message" style={{ marginBottom: '1rem' }}>{feedback}</div>}

      <div style={{ display: 'flex', gap: '1rem', marginBottom: '2rem' }}>
        <button className="search-btn" onClick={() => handleCompare(companies[0], companies[1])}>
          <i className="fas fa-scale-balanced"></i> Compare Companies
        </button>
      </div>

      <div style={{ overflowX: 'auto' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ borderBottom: '2px solid #2f5577', color: '#adccf0' }}>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Company</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Rating</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Reviews</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Culture</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Salary</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Growth</th>
              <th style={{ padding: '0.8rem', textAlign: 'left' }}>Actions</th>
            </tr>
          </thead>
          <tbody>
            {companies.map(company => (
              <tr key={company.id} style={{ borderBottom: '1px dotted #253e58' }}>
                <td style={{ padding: '0.8rem' }}>{company.name}</td>
                <td style={{ padding: '0.8rem' }}>
                  {'⭐'.repeat(Math.floor(company.rating))} {company.rating}
                </td>
                <td style={{ padding: '0.8rem' }}>{company.reviews.toLocaleString()}</td>
                <td style={{ padding: '0.8rem' }}>{company.culture}</td>
                <td style={{ padding: '0.8rem' }}>{company.salary}</td>
                <td style={{ padding: '0.8rem' }}>{company.growth}</td>
                <td style={{ padding: '0.8rem' }}>
                  <button
                    onClick={() => handleViewReviews(company)}
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
                    <i className="fas fa-star"></i> Reviews
                  </button>
                  <button
                    onClick={() => setSelectedCompany(company)}
                    style={{
                      background: '#2d4b6e',
                      border: 'none',
                      borderRadius: '20px',
                      padding: '0.3rem 1rem',
                      color: 'white',
                      cursor: 'pointer'
                    }}
                  >
                    <i className="fas fa-info-circle"></i> Details
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {selectedCompany && (
        <div className="stat-panel" style={{ marginTop: '2rem' }}>
          <div className="panel-header">
            <i className="fas fa-building"></i> {selectedCompany.name} Details
          </div>
          <p><strong>Rating:</strong> {selectedCompany.rating}/5 ({selectedCompany.reviews} reviews)</p>
          <p><strong>Culture:</strong> {selectedCompany.culture}</p>
          <p><strong>Salary:</strong> {selectedCompany.salary}</p>
          <p><strong>Growth:</strong> {selectedCompany.growth}</p>
          <button
            className="search-btn"
            style={{ marginTop: '1rem' }}
            onClick={() => setSelectedCompany(null)}
          >
            Close
          </button>
        </div>
      )}
    </div>
  );
};

export default CompanyResearch;