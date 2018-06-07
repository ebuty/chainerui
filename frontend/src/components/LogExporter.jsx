import React from 'react';
import PropTypes from 'prop-types';
import { Button } from 'reactstrap';
import {
  getLogData,
  getUrlSafeProjectNameFull,
  downloadObjectAsJson,
  yyyymmddhhmmss
} from '../utils';

class LogExporter extends React.Component {
  constructor(props) {
    super(props);

    this.handleClickDownloadJSON = this.handleClickDownloadJSON.bind(this);
    this.handleClickDownloadPNG = this.handleClickDownloadPNG.bind(this);
  }

  handleClickDownloadJSON() {
    const { project, results, stats, projectConfig } = this.props;
    const data = getLogData(results, stats, projectConfig);
    const exportName = `${getUrlSafeProjectNameFull(project)}_${yyyymmddhhmmss(new Date())}`;
    downloadObjectAsJson(data, exportName);
    console.log(project);
  }

  handleClickDownloadPNG() {
    console.log('downloading png...');
    console.log(this);
  }

  render() {
    return (
      <div>
        <Button size="xs" className="m-1" onClick={this.handleClickDownloadJSON}>
          <span className="mx-1 oi oi-data-transfer-download" />json
        </Button>
        <Button size="xs" className="m-1" onClick={this.handleClickDownloadPNG}>
          <span className="mx-1 oi oi-data-transfer-download" />png
        </Button>
      </div>
    );
  }
}

LogExporter.propTypes = {
  project: PropTypes.shape({
    id: PropTypes.number,
    name: PropTypes.string,
    pathName: PropTypes.string
  }).isRequired,
  results: PropTypes.objectOf(PropTypes.any).isRequired,
  stats: PropTypes.shape({
    logKeys: PropTypes.arrayOf(PropTypes.string),
    xAxisKeys: PropTypes.arrayOf(PropTypes.string)
  }).isRequired,
  projectConfig: PropTypes.shape({
    axes: PropTypes.objectOf(PropTypes.shape({
      axisName: PropTypes.string,
      logKeysConfig: PropTypes.objectOf(PropTypes.shape({
        selected: PropTypes.bool
      }))
    })),
    resultsConfig: PropTypes.objectOf(PropTypes.shape({
      hidden: PropTypes.bool
    })),
    lines: PropTypes.objectOf(
      PropTypes.shape({
        resultId: PropTypes.number,
        logKey: PropTypes.string,
        config: PropTypes.shape({
          color: PropTypes.string,
          isVisible: PropTypes.bool
        })
      })
    )
  }).isRequired
};

export default LogExporter;
