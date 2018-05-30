package org.irods.jargon.dataone.auth.endpoint;

import org.dataone.service.exceptions.NotAuthorized;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.servlet.http.HttpServletRequest;

/**
 * An authorization checker that doesn't check for authorization at all. This class should only be used
 * in member node service implementations that do not require authentication and authorization at all.
 * One example of this would be a member node service that resides behind a reverse proxy where the
 * response status code and response body are generated by the reverse proxy when authorization fails.
 *
 * @author Sarah Roberts - CyVerse
 */
public class AlwaysAllowAuthChecker implements AuthChecker {

    private Logger logger = LoggerFactory.getLogger(this.getClass());

    @Override
    public void checkAuthorization(HttpServletRequest request) throws NotAuthorized {
        logger.debug("ignoring authentication information in request");
    }
}
