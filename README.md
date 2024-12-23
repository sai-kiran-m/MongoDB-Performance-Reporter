# MongoDB Performance Reporter

## Author: Sai Kiran Mudunuru

## Overview
MongoDB Performance Reporter is a tool designed to generate and send performance reporting emails to teams managing collections on MongoDB Atlas. This tool aims to provide actionable insights for improving query performance and ensuring efficient database operations.

## Use Case
Teams with collections on MongoDB Atlas often require timely performance insights to identify bottlenecks and optimize their database usage. This tool analyzes the performance of collections, highlights areas of concern, and suggests improvements to enhance querying efficiency.

## Current Status
**In Progress**

## Features
### 1. Recommended Indices
- **Purpose**: Suggests indices to improve query performance based on collection usage patterns identified by MongoDB Atlas.
- **Functionality**:
  - Detects collections with high query usage.
  - Provides a list of indices that are recommended to reduce query latency.
  - Enables database administrators and developers to update collections for optimized performance.

## Upcoming Features
- **Email Scheduling**: Automatically send performance reports to relevant teams at predefined intervals.
- **Reporting Slow Queries**: Send reports to teams of their slow running queries.
- **Unused Indices**: Send reports to team of their unused indices, these unused indices takes up unncessary space on clusters and delay cluster recreation/update.
- **Integration with CI/CD Pipelines**: Seamlessly incorporate performance recommendations into deployment workflows.

## How to Use
1. **Setup**: Clone the repository and configure your MongoDB Atlas credentials.
2. **Run the Tool**: Execute the performance reporter script to generate insights.
3. **Apply Recommendations**: Review and implement suggested indices for improved query performance.

## Roadmap
- Add email notification functionality.
- Support for multi-cluster reporting.

## Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your enhancements or fixes.

## License
This project is licensed under the MIT License.

---

Feel free to suggest additional features or report issues.
