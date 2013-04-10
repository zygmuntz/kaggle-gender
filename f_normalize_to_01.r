normalize_to_01 <- function( p ) {

	max_p = max( p )
	min_p = min( p )

	p_norm = p - min_p
	p_norm = p_norm / ( max_p - min_p )
	
	return( p_norm )
	
}

