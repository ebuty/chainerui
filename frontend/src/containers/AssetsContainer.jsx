import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { Container } from 'reactstrap';

import * as uiPropTypes from '../store/uiPropTypes';
import {
  getResultAsset,
  updateGlobalPollingRate,
  updateGlobalChartSize,
  updateGlobalLogsLimit,
  updateGlobalResultNameAlignment
} from '../actions';
import NavigationBar from '../components/NavigationBar';
import AssetsTable from '../components/AssetsTable';

class AssetsContainer extends React.Component {
  componentDidMount() {
    const { projectId, resultId } = this.props;
    this.props.getResultAsset(projectId, resultId);
  }

  render() {
    const {
      assets, globalConfig, fetchState
    } = this.props;
    return (
      <div>
        <NavigationBar
          fetchState={fetchState}
          globalConfig={globalConfig}
          onGlobalConfigLogsLimitUpdate={this.props.updateGlobalLogsLimit}
          onGlobalConfigPollingRateUpdate={this.props.updateGlobalPollingRate}
          onGlobalConfigChartSizeUpdate={this.props.updateGlobalChartSize}
          onGlobalConfigResultNameAlignmentUpdate={this.props.updateGlobalResultNameAlignment}
        />
        <Container>
          <AssetsTable assets={assets} />
        </Container>
      </div>
    );
  }
}

const mapStateToProps = (state, ownProps) => {
  const projectId = Number(ownProps.params.projectId);
  const resultId = Number(ownProps.params.resultId);
  const {
    entities,
    fetchState,
    config
  } = state;
  const { assets } = entities;
  const globalConfig = config.global;
  return { projectId, resultId, assets, fetchState, globalConfig };
};

AssetsContainer.propTypes = {
  projectId: uiPropTypes.projectId.isRequired,
  resultId: uiPropTypes.resultId.isRequired,
  assets: uiPropTypes.assets.isRequired,
  fetchState: uiPropTypes.fetchState.isRequired,
  globalConfig: uiPropTypes.globalConfig.isRequired,
  getResultAsset: PropTypes.func.isRequired,
  updateGlobalPollingRate: PropTypes.func.isRequired,
  updateGlobalChartSize: PropTypes.func.isRequired,
  updateGlobalResultNameAlignment: PropTypes.func.isRequired,
  updateGlobalLogsLimit: PropTypes.func.isRequired
};

export default connect(mapStateToProps, {
  getResultAsset,
  updateGlobalPollingRate,
  updateGlobalChartSize,
  updateGlobalLogsLimit,
  updateGlobalResultNameAlignment
})(AssetsContainer);
